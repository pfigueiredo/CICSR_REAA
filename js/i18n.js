(function () {
  const SUPPORTED = ["pt", "en", "fr", "ar"];
  const DEFAULT_LOCALE = "pt";
  const RTL_LOCALES = ["ar"];

  function resolveLocale() {
    const params = new URLSearchParams(window.location.search);
    const fromUrl = params.get("lang");
    if (fromUrl && SUPPORTED.includes(fromUrl)) {
      return fromUrl;
    }
    const stored = localStorage.getItem("ciscsr-lang");
    if (stored && SUPPORTED.includes(stored)) {
      return stored;
    }
    const browser = (navigator.language || "").slice(0, 2).toLowerCase();
    if (SUPPORTED.includes(browser)) {
      return browser;
    }
    return DEFAULT_LOCALE;
  }

  function getNested(obj, key) {
    return key.split(".").reduce((acc, part) => {
      if (acc && Object.prototype.hasOwnProperty.call(acc, part)) {
        return acc[part];
      }
      return undefined;
    }, obj);
  }

  function applyList(container, items) {
    if (!Array.isArray(items)) {
      return;
    }
    container.innerHTML = "";
    items.forEach((text) => {
      const li = document.createElement("li");
      li.textContent = text;
      container.appendChild(li);
    });
  }

  function applyMembers(container, items) {
    if (!Array.isArray(items)) {
      return;
    }
    container.innerHTML = "";
    items.forEach((item) => {
      const row = document.createElement("div");
      row.className = "member-row";

      const name = document.createElement("strong");
      name.textContent = item.name || "";
      row.appendChild(name);

      if (item.sgc) {
        const sgc = document.createElement("span");
        sgc.className = "member-sgc";
        sgc.textContent = item.sgc;
        row.appendChild(sgc);
      }

      const meta = document.createElement("span");
      meta.className = "member-meta";
      meta.textContent = item.meta || "";
      row.appendChild(meta);

      container.appendChild(row);
    });
  }

  function applyEvents(container, items) {
    if (!Array.isArray(items)) {
      return;
    }
    container.innerHTML = "";
    if (items.length === 0) {
      return;
    }
    const list = document.createElement("ul");
    list.className = "event-list";
    items.forEach((item) => {
      const li = document.createElement("li");
      li.className = "event-item";

      const head = document.createElement("div");
      head.className = "event-item-head";

      const date = document.createElement("time");
      date.textContent = item.date || "";
      head.appendChild(date);

      if (item.place) {
        const place = document.createElement("span");
        place.className = "event-place";
        place.textContent = item.place;
        head.appendChild(place);
      }

      li.appendChild(head);

      if (item.text) {
        const text = document.createElement("p");
        text.textContent = item.text;
        li.appendChild(text);
      }

      list.appendChild(li);
    });
    container.appendChild(list);
  }

  function applySignatories(container, items) {
    if (!Array.isArray(items)) {
      return;
    }
    container.innerHTML = "";
    items.forEach((text) => {
      const p = document.createElement("p");
      p.textContent = text;
      container.appendChild(p);
    });
  }

  function applyTranslations(strings, locale) {
    document.documentElement.lang = locale;
    document.documentElement.dir = RTL_LOCALES.includes(locale) ? "rtl" : "ltr";

    const title = getNested(strings, "meta.title");
    const description = getNested(strings, "meta.description");
    if (title) {
      document.title = title;
    }
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc && description) {
      metaDesc.setAttribute("content", description);
    }

    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      const value = getNested(strings, key);
      if (value === undefined) {
        return;
      }
      if (el.hasAttribute("data-i18n-html")) {
        el.innerHTML = value;
      } else {
        el.textContent = value;
      }
    });

    document.querySelectorAll(".speech-ar-note").forEach((el) => {
      el.hidden = !el.textContent.trim();
    });

    document.querySelectorAll("[data-i18n-attr]").forEach((el) => {
      const pairs = el.getAttribute("data-i18n-attr").split(";");
      pairs.forEach((pair) => {
        const [attr, key] = pair.split(":").map((s) => s.trim());
        const value = getNested(strings, key);
        if (value !== undefined && attr) {
          el.setAttribute(attr, value);
        }
      });
    });

    document.querySelectorAll("[data-i18n-list]").forEach((el) => {
      const key = el.getAttribute("data-i18n-list");
      applyList(el, getNested(strings, key));
    });

    document.querySelectorAll("[data-i18n-signatories]").forEach((el) => {
      const key = el.getAttribute("data-i18n-signatories");
      applySignatories(el, getNested(strings, key));
    });

    document.querySelectorAll("[data-i18n-members]").forEach((el) => {
      const key = el.getAttribute("data-i18n-members");
      applyMembers(el, getNested(strings, key));
    });

    document.querySelectorAll("[data-i18n-events]").forEach((el) => {
      const key = el.getAttribute("data-i18n-events");
      applyEvents(el, getNested(strings, key));
    });

    document.querySelectorAll(".lang-switcher button").forEach((btn) => {
      const isActive = btn.dataset.lang === locale;
      btn.classList.toggle("is-active", isActive);
      btn.setAttribute("aria-pressed", String(isActive));
    });
  }

  function updateUrl(locale) {
    const url = new URL(window.location.href);
    url.searchParams.set("lang", locale);
    window.history.replaceState({}, "", url);
  }

  function getSiteRoot() {
    const el = document.querySelector('script[src*="i18n.js"]');
    if (!el) {
      return "";
    }
    const src = el.getAttribute("src") || "";
    return src.replace(/js\/i18n\.js(?:\?.*)?$/, "");
  }

  function currentLocale() {
    return localStorage.getItem("ciscsr-lang") || resolveLocale();
  }

  function preserveLangOnNavigate(event) {
    const anchor = event.target.closest("a[href]");
    if (!anchor || event.defaultPrevented || event.button !== 0) {
      return;
    }
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
      return;
    }
    const raw = anchor.getAttribute("href");
    if (!raw || /^(https?:|mailto:|tel:)/i.test(raw)) {
      return;
    }
    if (raw.startsWith("#")) {
      return;
    }
    let url;
    try {
      url = new URL(raw, window.location.href);
    } catch (err) {
      return;
    }
    if (url.origin !== window.location.origin) {
      return;
    }
    const locale = currentLocale();
    if (!SUPPORTED.includes(locale)) {
      return;
    }
    url.searchParams.set("lang", locale);
    event.preventDefault();
    window.location.assign(url.href);
  }

  async function loadLocale(locale) {
    const response = await fetch(`${getSiteRoot()}locales/${locale}.json`, {
      cache: "no-cache",
    });
    if (!response.ok) {
      throw new Error(`Failed to load locale: ${locale}`);
    }
    return response.json();
  }

  async function setLocale(locale) {
    if (!SUPPORTED.includes(locale)) {
      locale = DEFAULT_LOCALE;
    }
    const strings = await loadLocale(locale);
    localStorage.setItem("ciscsr-lang", locale);
    applyTranslations(strings, locale);
    updateUrl(locale);
    document.dispatchEvent(new CustomEvent("localechange", { detail: { locale, strings } }));
  }

  function buildLangSwitcher() {
    const container = document.querySelector(".lang-switcher");
    if (!container) {
      return;
    }
    const labels = { pt: "PT", en: "EN", fr: "FR", ar: "AR" };
    container.innerHTML = "";
    SUPPORTED.forEach((code, index) => {
      if (index > 0) {
        const sep = document.createElement("span");
        sep.textContent = "|";
        sep.setAttribute("aria-hidden", "true");
        container.appendChild(sep);
      }
      const btn = document.createElement("button");
      btn.type = "button";
      btn.dataset.lang = code;
      btn.textContent = labels[code];
      btn.setAttribute("aria-label", code.toUpperCase());
      btn.addEventListener("click", () => setLocale(code));
      container.appendChild(btn);
    });
  }

  document.addEventListener("click", preserveLangOnNavigate);

  document.addEventListener("DOMContentLoaded", async () => {
    buildLangSwitcher();
    try {
      await setLocale(resolveLocale());
    } catch (err) {
      console.error(err);
      await setLocale(DEFAULT_LOCALE);
    }
  });

  window.CISCSR_I18N = { setLocale, resolveLocale, SUPPORTED };
})();

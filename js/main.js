const button = document.querySelector(".menu-button");
const nav = document.querySelector(".main-nav");

function setMenuOpen(open) {
  if (!button || !nav) {
    return;
  }
  nav.classList.toggle("open", open);
  button.setAttribute("aria-expanded", String(open));
}

if (button && nav) {
  button.addEventListener("click", () => {
    setMenuOpen(!nav.classList.contains("open"));
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setMenuOpen(false));
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setMenuOpen(false);
    }
  });

  document.addEventListener("click", (event) => {
    if (!nav.classList.contains("open")) {
      return;
    }
    if (nav.contains(event.target) || button.contains(event.target)) {
      return;
    }
    setMenuOpen(false);
  });
}

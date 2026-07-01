"""Capture presentation screenshots from the live CISCSR site."""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "https://pfigueiredo.github.io/CICSR_REAA/"
OUT = Path(__file__).resolve().parent.parent / "presentation" / "assets" / "screenshots"
OUT.mkdir(parents=True, exist_ok=True)


def shot(page, name, url=None, width=1280, height=900, selector=None, full_page=False):
    page.set_viewport_size({"width": width, "height": height})
    page.goto(url or BASE, wait_until="networkidle")
    page.wait_for_timeout(800)
    path = OUT / name
    if selector:
        el = page.locator(selector)
        el.scroll_into_view_if_needed()
        page.wait_for_timeout(400)
        el.screenshot(path=str(path))
    else:
        page.screenshot(path=str(path), full_page=full_page)
    print("wrote", path.name)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        shot(page, "hero-pt.png", selector=".hero")
        shot(page, "declaration-pt.png", selector="#declaracao")
        shot(page, "pillars.png", selector="#principios .principles")
        shot(page, "members-dark.png", selector="#membros")
        shot(page, "arabic-rtl.png", url=BASE + "?lang=ar", full_page=False)
        shot(page, "mobile.png", url=BASE + "?lang=pt", width=390, height=844, selector=".hero")

        browser.close()


if __name__ == "__main__":
    main()

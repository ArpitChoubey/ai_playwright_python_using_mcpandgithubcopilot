from playwright.sync_api import Page


class BasePage:
    """Simple base page providing common utilities.

    The page object holds a Playwright Page instance and exposes helpers for
    navigation and waiting.
    """

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str, timeout: int = 30000):
        self.page.goto(url, timeout=timeout)

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            return self.page.is_visible(selector)
        except Exception:
            return False

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)


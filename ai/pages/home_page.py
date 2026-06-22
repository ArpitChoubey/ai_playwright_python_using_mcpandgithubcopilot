from playwright.sync_api import Page
from .base_page import BasePage


class HomePage(BasePage):
    """Page object for Demoblaze home page (https://www.demoblaze.com)

    Encapsulates selectors and user actions for login/logout flow.
    """

    URL = "https://www.demoblaze.com/index.html"

    # Selectors
    LOGIN_LINK = "#login2"
    LOGOUT_LINK = "#logout2"
    NAME_OF_USER = "#nameofuser"
    LOGIN_MODAL = "#logInModal"
    LOGIN_USERNAME = "#loginusername"
    LOGIN_PASSWORD = "#loginpassword"
    LOGIN_MODAL_SUBMIT = "#logInModal .modal-footer button.btn-primary"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.goto(self.URL)

    def click_login_link(self):
        self.click(self.LOGIN_LINK)

    def login(self, username: str, password: str):
        # Click login link to show modal
        self.click_login_link()
        # Wait for modal inputs
        self.page.wait_for_selector(self.LOGIN_USERNAME, timeout=10000)
        self.fill(self.LOGIN_USERNAME, username)
        self.fill(self.LOGIN_PASSWORD, password)
        # Click login button in modal
        self.click(self.LOGIN_MODAL_SUBMIT)

    def is_logged_in(self, username: str) -> bool:
        # Wait for nameofuser to be visible
        try:
            self.page.wait_for_selector(self.NAME_OF_USER, timeout=10000)
            text = self.page.inner_text(self.NAME_OF_USER)
            return username in text
        except Exception:
            return False

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def is_login_link_visible(self) -> bool:
        return self.is_visible(self.LOGIN_LINK)


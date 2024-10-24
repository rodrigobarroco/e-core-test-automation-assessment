import re
from playwright.sync_api import Page, expect
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

class LoginPage:
    # Constants for locators
    USERNAME_SELECTOR = 'input[name="username"]'  # Locator for username input field
    PASSWORD_SELECTOR = 'input[name="password"]'  # Locator for password input field
    LOGIN_BUTTON_SELECTOR = '#btnLogin'  # Locator for login button
    ERROR_MESSAGE_SELECTOR = 'div.alert.alert-danger.mt-3'  # Locator for the error message

    def __init__(self, page: Page):
        """Initialize the LoginPage class with a Playwright page instance."""
        self.page = page

    def navigate(self):
        """Navigate to the base URL and wait until the network is idle."""
        self.page.goto(Config.BASE_URL)  # Go to the base URL
        self.page.wait_for_load_state('networkidle', timeout=Config.TIMEOUT * 1000)  # Wait for the page to fully load

    def login(self, credentials: UserCredentialsDTO):
        """Fill in the username and password fields and click the login button."""
        self.page.fill(self.USERNAME_SELECTOR, credentials.username)  # Enter the username
        self.page.fill(self.PASSWORD_SELECTOR, credentials.password)  # Enter the password
        self.page.click(self.LOGIN_BUTTON_SELECTOR)  # Click the login button

    def get_error_message(self):
        """Return the error message text if login fails."""
        error_message = self.page.locator(self.ERROR_MESSAGE_SELECTOR)  # Locate the error message element
        return error_message.text_content().strip() if error_message.is_visible() else None  # Return the error message if visible, else return None

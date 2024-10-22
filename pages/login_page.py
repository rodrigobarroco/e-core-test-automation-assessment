import re
from playwright.sync_api import Page, expect
from dto.user_credentials_dto import UserCredentialsDTO
from dto.config_dto import ConfigDTO

class LoginPage:
    USERNAME_SELECTOR = 'input[name="username"]'
    PASSWORD_SELECTOR = 'input[name="password"]'
    LOGIN_BUTTON_SELECTOR = '#btnLogin'

    def __init__(self, page: Page, config: ConfigDTO):  # Add config parameter
        self.page = page
        self.config = config

    def navigate(self):
        # Use the base_url from the config DTO
        self.page.goto(self.config.base_url)
        self.page.wait_for_load_state('networkidle')  # Ensure the page is fully loaded

    def login(self, credentials: UserCredentialsDTO):
        self.page.fill(self.USERNAME_SELECTOR, credentials.username)
        self.page.fill(self.PASSWORD_SELECTOR, credentials.password)
        self.page.click(self.LOGIN_BUTTON_SELECTOR)

    def get_error_message(self):
        return self.page.locator("div.error").text_content()

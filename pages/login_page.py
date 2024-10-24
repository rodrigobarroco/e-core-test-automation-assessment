import re
from playwright.sync_api import Page, expect
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

class LoginPage:
    USERNAME_SELECTOR = 'input[name="username"]'
    PASSWORD_SELECTOR = 'input[name="password"]'
    LOGIN_BUTTON_SELECTOR = '#btnLogin'

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(Config.BASE_URL)
        self.page.wait_for_load_state('networkidle', timeout=Config.TIMEOUT * 1000)

    def login(self, credentials: UserCredentialsDTO):
        self.page.fill(self.USERNAME_SELECTOR, credentials.username)
        self.page.fill(self.PASSWORD_SELECTOR, credentials.password)
        self.page.click(self.LOGIN_BUTTON_SELECTOR)

    def get_error_message(self):
        return self.page.locator('div.alert.alert-danger.mt-3').text_content().strip()

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

valid_credentials = UserCredentialsDTO("demouser", "abc123")

def perform_successful_login(page: Page, login_page: LoginPage):
    login_page.navigate()  
    login_page.login(valid_credentials)
    expected_url = f"{Config.BASE_URL}/account"
    assert page.url == expected_url, f"Login with valid credentials failed for {valid_credentials.username}"
    header = page.locator('h2.mt-5')
    expect(header).to_have_text("Invoice List")

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    perform_successful_login(page, login_page)

def test_failed_login(browser):
    credentials_list = [
        UserCredentialsDTO("Demouser", "abc123"),  # Invalid
        UserCredentialsDTO("demouser_", "xyz"),    # Invalid
        UserCredentialsDTO("demouser", "nananana"),# Invalid
        valid_credentials                          # Valid
    ]
    for credentials in credentials_list:
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        if credentials == valid_credentials:
            perform_successful_login(page, login_page)        
        else:           
            login_page.navigate()
            login_page.login(credentials)
            error_message = login_page.get_error_message()
            assert error_message == "Wrong username or password.", f"Expected error message not found for {credentials.username}"
        context.close()

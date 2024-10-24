import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

# Valid login credentials
valid_credentials = UserCredentialsDTO("demouser", "abc123")

# Helper function to perform a successful login and verify the login process
def perform_successful_login(page: Page, login_page: LoginPage):
    login_page.navigate()  
    login_page.login(valid_credentials)
    
    # Check that the page URL matches the expected account page URL after login
    expected_url = f"{Config.BASE_URL}/account"
    assert page.url == expected_url, f"Login with valid credentials failed for {valid_credentials.username}"
    
    # Verify the page content contains 'Invoice List'
    header = page.locator('h2.mt-5')
    expect(header).to_have_text("Invoice List")

# Test to ensure login with valid credentials works
def test_successful_login(page: Page):
    login_page = LoginPage(page)
    perform_successful_login(page, login_page)

# Test multiple invalid login attempts and verify the correct error message
def test_failed_login(browser):
    credentials_list = [
        UserCredentialsDTO("Demouser", "abc123"),  # Invalid username (case-sensitive)
        UserCredentialsDTO("demouser_", "xyz"),    # Invalid username and password
        UserCredentialsDTO("demouser", "nananana"),# Incorrect password
        valid_credentials                          # Valid credentials
    ]

    for credentials in credentials_list:
        # Open a new context and page for each test run
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        
        if credentials == valid_credentials:
            # Perform a successful login with valid credentials
            perform_successful_login(page, login_page)        
        else:
            # Attempt invalid login and verify the error message
            login_page.navigate()
            login_page.login(credentials)
            error_message = login_page.get_error_message()
            assert error_message == "Wrong username or password.", f"Expected error message not found for {credentials.username}"
        
        # Close the context after each test run
        context.close()

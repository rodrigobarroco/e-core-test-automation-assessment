import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

# Define valid credentials once
valid_credentials = UserCredentialsDTO("demouser", "abc123")

def perform_successful_login(page: Page, login_page: LoginPage):
    # Step 1: Navigate to the login page
    login_page.navigate()
    
    # Step 2: Perform login with valid credentials
    login_page.login(valid_credentials)

    # Step 3: Verify the login result (URL or content checks)
    expected_url = f"{Config.BASE_URL}/account"
    assert page.url == expected_url, f"Login with valid credentials failed for {valid_credentials.username}"

    # Step 4: Verify the "Invoice List" text on the page
    header = page.locator('h2.mt-5')
    expect(header).to_have_text("Invoice List")

def test_successful_login(page: Page):
    # Initialize the LoginPage
    login_page = LoginPage(page)

    # Perform login and verification using the helper function
    perform_successful_login(page, login_page)

def test_failed_login(browser):
    # List of credentials (1 valid and the rest invalid)
    credentials_list = [
        UserCredentialsDTO("Demouser", "abc123"),  # Invalid
        UserCredentialsDTO("demouser_", "xyz"),    # Invalid
        UserCredentialsDTO("demouser", "nananana"),# Invalid
        valid_credentials                          # Valid
    ]

    # Step 2: Iterate over each set of credentials (valid and invalid)
    for credentials in credentials_list:
        # Open a new browser context and new page for each login attempt
        context = browser.new_context()
        page = context.new_page()

        # Initialize the LoginPage with the new page
        login_page = LoginPage(page)

        # Step 1: Check whether it's a valid or invalid credential set
        if credentials == valid_credentials:
            # Use the shared helper function to verify the valid login
            perform_successful_login(page, login_page)        

        else:
            # Navigate to the login page
            login_page.navigate()

            # Attempt login with credentials
            login_page.login(credentials)

            # Step 2: Assert that the error message is displayed for invalid credentials
            error_message = login_page.get_error_message()
            assert error_message == "Wrong username or password.", f"Expected error message not found for {credentials.username}"

        # Close the context to clean up for the next iteration
        context.close()

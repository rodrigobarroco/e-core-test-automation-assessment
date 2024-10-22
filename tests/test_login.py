import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from dto.user_credentials_dto import UserCredentialsDTO
from dto.config_dto import ConfigDTO

def test_login_positive(page: Page):
    # Create the ConfigDTO with the base URL
    config = ConfigDTO(base_url="https://automation-sandbox-python-mpywqjbdza-uc.a.run.app")
    
    # Initialize the LoginPage with the config
    login_page = LoginPage(page, config)

    # Step 1: Navigate to the login page
    login_page.navigate()
    
    # Step 2: Enter credentials and submit
    valid_credentials = UserCredentialsDTO("demouser", "abc123")
    login_page.login(valid_credentials)

    # Step 3: Verify that the login was successful and the user is redirected to the correct URL
    expected_url = f"{config.base_url}/account"
    assert page.url == expected_url

    # Step 4: Verify if the text "Invoice List" is present in the <h2> element
    header = page.locator('h2.mt-5')
    expect(header).to_have_text("Invoice List")


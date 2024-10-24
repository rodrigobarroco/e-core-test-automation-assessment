import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Add parent directory to the system path for module imports
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage  # Import the LoginPage class
from pages.invoice_page import InvoicePage  # Import the InvoicePage class
from pages.account_page import AccountPage  # Import the AccountPage class
from dto.user_credentials_dto import UserCredentialsDTO  # Import user credentials data object
from utils.config import Config  # Import configuration utility

# Test for validating the invoice list details
def test_validate_invoice_list(page: Page):
    login_page = LoginPage(page)  # Initialize the login page
    login_page.navigate()  # Navigate to the login page
    valid_credentials = UserCredentialsDTO("demouser", "abc123")  # Use demo user credentials
    login_page.login(valid_credentials)  # Perform the login with the provided credentials
    
    # Navigate to the account page and validate the invoice list details
    account_page = AccountPage(page)
    account_page.assert_invoice_list([  # List of expected values to be validated on the invoice list
        "Invoice List",
        "Invoice Number",
        "Hotel Name",
        "Invoice Date",
        "Due Date",
        "Invoice Link",
        "110",
        "Rendezvous Hotel",
        "14/01/2018",
        "15/01/2018",
        "Invoice Details",
        "110",
        "Rendezvous Hotel 1",
        "14/01/2018",
        "15/01/2018",
        "Invoice Details"
    ])

# Test for validating the invoice details
def test_validate_invoice_details(page: Page):
    login_page = LoginPage(page)  # Initialize the login page
    login_page.navigate()  # Navigate to the login page
    valid_credentials = UserCredentialsDTO("demouser", "abc123")  # Use demo user credentials
    login_page.login(valid_credentials)  # Perform the login with the provided credentials
    
    # Navigate to the invoice page and validate the details
    invoice_page = InvoicePage(page)
    invoice_page.assert_invoice_details([  # List of expected values to be validated on the invoice details page
        "Invoice Details",  
        "Rendezvous Hotel",  
        "Invoice #110 details",  
        "Invoice Date:",  
        "14/01/2018",  
        "Due Date:",  
        "15/01/2018",  
        "Booking/Stay details",  
        "Booking Code",  
        "0875",  
        "Room",  
        "Superior Double",  
        "Total Stay Count",  
        "1",  
        "Total Stay Amount",  
        "$150",  
        "Check-In",  
        "14/01/2018",  
        "Check-Out",  
        "15/01/2018",  
        "Customer Details",  
        "JOHNY SMITH",  
        "R2, AVENUE DU MAROC",  
        "123456",  
        "Billing Details",  
        "Deposit Nowt",  
        "Tax&VAT",  
        "Total Amount",  
        "USD $20.90",  
        "USD $19",  
        "USD $209"
    ])

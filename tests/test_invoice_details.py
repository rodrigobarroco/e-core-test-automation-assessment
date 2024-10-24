import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.invoice_page import InvoicePage
from pages.account_page import AccountPage
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

def test_validate_invoice_details(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    valid_credentials = UserCredentialsDTO("demouser", "abc123")
    login_page.login(valid_credentials)
    account_page = AccountPage(page)
    account_page.assert_invoice_list(["Invoice List",
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

def test_validate_invoice_details(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    valid_credentials = UserCredentialsDTO("demouser", "abc123")
    login_page.login(valid_credentials)
    invoice_page = InvoicePage(page)
    invoice_page.assert_invoice_details([
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
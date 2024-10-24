import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.invoice_page import InvoicePage
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

def test_validate_invoice_details(page: Page):
    # Step 1: Perform login
    login_page = LoginPage(page)
    login_page.navigate()
    valid_credentials = UserCredentialsDTO("demouser", "abc123")
    login_page.login(valid_credentials)

    # Step 2: Navigate to the invoice page (after successful login)
    invoice_page = InvoicePage(page)

    # Wait for the "Invoice List" page to load
    invoice_list_element = page.get_by_role("heading", name="Invoice List")
    assert invoice_list_element.is_visible(), "Failed to load Invoice List page"

    # Step 3: Assert that the hotel name, invoice date, and due date are correct
    hotel_name_element = page.get_by_text("Rendezvous Hotel", exact=True)
    assert hotel_name_element.is_visible(), "Hotel Name is not visible or incorrect"
    
    invoice_date_element = page.get_by_text("14/01/").first
    assert invoice_date_element.is_visible(), "Invoice Date is not visible or incorrect"
    
    invoice_date_element = page.get_by_text("15/01/").first
    assert invoice_date_element.is_visible(), "Due Date is not visible or incorrect"

    # Step 4: Click the "Invoice Details" button
    invoice_details_button = page.get_by_role("link", name="Invoice Details").first
    invoice_details_button.click()
    page.wait_for_timeout(3000)

    # Step 5: Validate the invoice details on the next page
    invoice_page.assert_section_value([
    "Invoice List",
    "Hotel Name",
    "Rendezvous Hotel",
    "Invoice Date",
    "14/01/2018",
    "Due Date",
    "15/01/2018",
    "Invoice Number",
    "110"
    ])
    invoice_page.assert_booking_code()
    #invoice_page.assert_customer_details()
    #invoice_page.assert_room()
    #invoice_page.assert_checkin()
    #invoice_page.assert_checkout()
    #invoice_page.assert_total_stay_count()
    #invoice_page.assert_total_stay_amount()
    #invoice_page.assert_deposit_now()
    #invoice_page.assert_tax_vat()
    #invoice_page.assert_total_amount()
    #invoice_page.assert_deposit_now_label()

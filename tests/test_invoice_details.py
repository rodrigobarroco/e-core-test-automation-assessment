import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.invoice_page import InvoicePage

def test_invoice_details(page: Page):
    login_page = LoginPage(page)
    invoice_page = InvoicePage(page)

    # Step 1: Login
    login_page.navigate("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app")
    login_page.login("demouser", "abc123")

    # Step 2: Click the first invoice link
    invoice_page.click_invoice_link()

    # Step 3: Validate the invoice details
    expected_invoice = {
        "hotel_name": "Rendezvous Hotel",
        "invoice_date": "14/01/2018",
        "due_date": "15/01/2018",
        "invoice_number": "110",
        "booking_code": "0875",
        "customer_details": "JOHNY SMITH",
        "room": "Superior Double",
        "check_in": "14/01/2018",
        "check_out": "15/01/2018",
        "total_stay_count": "1",
        "total_stay_amount": "$150",
        "deposit_now": "USD $20.90",
        "tax_vat": "USD $19.00",
        "total_amount": "USD $209.00"
    }

    actual_invoice = invoice_page.get_invoice_details()
    assert actual_invoice == expected_invoice

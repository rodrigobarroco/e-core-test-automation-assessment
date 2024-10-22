import re
from playwright.sync_api import Page, expect

class InvoicePage:
    def __init__(self, page: Page):
        self.page = page

    def click_invoice_link(self):
        self.page.click("a#invoice-details")  # Atualize com o seletor correto

    def get_invoice_details(self):
        invoice_details = {
            "hotel_name": self.page.locator("#hotelName").text_content(),
            "invoice_date": self.page.locator("#invoiceDate").text_content(),
            "due_date": self.page.locator("#dueDate").text_content(),
            "invoice_number": self.page.locator("#invoiceNumber").text_content(),
            "booking_code": self.page.locator("#bookingCode").text_content(),
            "customer_details": self.page.locator("#customerDetails").text_content(),
            "room": self.page.locator("#room").text_content(),
            "check_in": self.page.locator("#checkIn").text_content(),
            "check_out": self.page.locator("#checkOut").text_content(),
            "total_stay_count": self.page.locator("#totalStayCount").text_content(),
            "total_stay_amount": self.page.locator("#totalStayAmount").text_content(),
            "deposit_now": self.page.locator("#depositNow").text_content(),
            "tax_vat": self.page.locator("#taxVAT").text_content(),
            "total_amount": self.page.locator("#totalAmount").text_content(),
        }
        return invoice_details

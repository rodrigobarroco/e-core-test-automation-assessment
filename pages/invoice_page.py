import re
from playwright.sync_api import Page, expect
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

class InvoicePage:
    def __init__(self, page: Page):
        self.page = page


    def assert_section_value(self, section_values):
        section = self.page.locator("section")
        section_text = section.text_content().replace('\n', '').strip()
        print("Texto da section encontrado:", section_text)

        for value in section_values:
            assert value in section_text, f"'{value}' not visible in section"
            print(f"Validating: {value}")

    def assert_booking_code(self):
        booking_code = self.page.get_by_role("cell", name="0875")
        print("Booking Code:", booking_code.text_content())
        assert booking_code.is_visible(), "Booking Code '0875' not found"

    
    def assert_customer_details(self):
        section_text = self.page.locator("section").text_content().replace('\n', '').strip()
        print("Texto da section encontrado:", section_text)
        assert "JOHNY SMITHR2, AVENUE DU MAROC123456" in section_text, "Customer details not found or incorrect"

    
    def assert_room(self):
        assert self.page.get_by_role("cell", name="Superior Double").is_visible(), "Room 'Superior Double' not found"
    
    def assert_checkin(self):
        assert self.page.get_by_role("cell", name="14/01/").is_visible(), "Check-In Date '14/01/2018' not found"
    
    def assert_checkout(self):
        assert self.page.get_by_role("cell", name="15/01/").is_visible(), "Check-Out Date '15/01/2018' not found"
    
    def assert_total_stay_count(self):
        assert self.page.get_by_role("cell", name="1", exact=True).is_visible(), "Total Stay Count '1' not found"
    
    def assert_total_stay_amount(self):
        assert self.page.get_by_role("cell", name="$150").is_visible(), "Total Stay Amount '$150' not found"
    
    def assert_deposit_now(self):
        assert self.page.get_by_role("cell", name="USD $20.90").is_visible(), "Deposit Now 'USD $20.90' not found"
    
    def assert_tax_vat(self):
        assert self.page.get_by_role("cell", name="USD $19").is_visible(), "Tax & VAT 'USD $19' not found"
    
    def assert_total_amount(self):
        assert self.page.get_by_role("cell", name="USD $209").is_visible(), "Total Amount 'USD $209' not found"
    
    def assert_deposit_now_label(self):
        assert self.page.get_by_role("cell", name="Deposit Nowt").is_visible(), "Deposit Now label not found or incorrect"

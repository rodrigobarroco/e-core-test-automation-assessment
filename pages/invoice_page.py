import re
from playwright.sync_api import Page, expect
from dto.user_credentials_dto import UserCredentialsDTO
from utils.config import Config

class InvoicePage:
    def __init__(self, page: Page):
        self.page = page
         
    def assert_invoice_details(self, section_values):
        self.page.goto(f"{Config.BASE_URL}/invoice/0")
        section = self.page.locator("section")
        section_text = section.text_content().replace('\n', '').strip()
        print("Texto da section encontrado:", section_text)

        for value in section_values:
            assert value in section_text, f"'{value}' not visible in section"
            print(f"Validating: {value}")

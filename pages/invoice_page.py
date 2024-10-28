from playwright.sync_api import Page, expect
from utils.config import Config

class InvoicePage:
    """This class contains methods to interact with and validate elements on the invoice details page."""

    def __init__(self, page: Page):
        """Initialize the InvoicePage with a Playwright page object."""
        self.page = page
         
    def assert_invoice_details(self, section_values):
        """Asserts that all the expected values in the invoice details are present in the page's section."""
        # Navigate to the invoice details page
        self.page.goto(f"{Config.BASE_URL}/invoice/0")

        # Locate the section and extract its text content
        section = self.page.locator("section")
        section_text = section.text_content().replace('\n', '').strip()

        print("Texto da section encontrado:", section_text)

        # Loop through expected values and validate their presence in the section
        for value in section_values:
            assert value in section_text, f"'{value}' not visible in section"
            print(f"Validating: {value}")

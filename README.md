# E-Core Test Automation Assessment

This repository contains the test automation project for the E-Core assessment. It uses Playwright and PyTest to validate login functionality and invoice details on a sample web application.

# Project Structure

- `pages/`: Contains page object classes (`LoginPage`, `AccountPage`, `InvoicePage`) to interact with different parts of the web app.
- `dto/`: Data Transfer Object classes like `UserCredentialsDTO` to handle test data.
- `tests/`: Contains test scripts for validating login and invoice functionalities.
- `utils/`: Contains configuration (`Config`) for base URL and other settings.

# Prerequisites

- Python 3.12+
- Playwright
- PyTest

# Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/rodrigobarroco/e-core-test-automation-assessment.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Install Playwright browsers:
   ```bash
   playwright install
# Running Tests

- To run all tests, use:
   ```bash
   pytest
- For detailed output:
   ```bash
   pytest -s
- To run tests in headed mode:
   ```bash
   pytest --headed
# Project Design

This project follows the Page Object Model (POM) pattern for better maintainability and reusability.

## Key Tests
* `test_successful_login`: Verifies successful login with valid credentials.
* `test_failed_logins`: Tests login attempts with invalid credentials using parameterized inputs.
* `test_validate_invoice_list`: Verifies key invoice list post-login
* `test_validate_invoice_details`: Verifies key invoice details post-login.

# Configuration

The configuration is managed in `utils/config.py`, where base URL and browser settings are stored. You can update the URL or timeout settings here.

    class Config:
        BASE_URL = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app"
        TIMEOUT = 30  # Timeout for page load in seconds
        BROWSER = "chromium"  # Default browser
# Conclusion

This project demonstrates the ability to automate tests for login and invoice-related functionality using Playwright and PyTest. It follows best practices for test structure, readability, and reusability, ensuring efficient test automation.


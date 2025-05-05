import pytest
from pages.login_page import LoginPage
from utils.logger import log_result

@pytest.mark.usefixtures("browser")
class TestLogin:
    def test_valid_login(self, browser):
        try:
            browser.get("https://automationexercise.com")
            lp = LoginPage(browser)
            lp.login("testemail@example.com", "testpass")  # Use actual test creds

            assert "Logged in as" in browser.page_source
            log_result("test_valid_login", "PASS")
        except Exception as e:
            log_result("test_valid_login", "FAIL", str(e))
            browser.save_screenshot("screenshots/test_valid_login.png")
            raise

import os
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page    import LoginPage
from pages.register_page import RegisterPage
from utils.logger        import log_result

@pytest.mark.usefixtures("browser")
class TestLogin:
    def test_login_or_register(self, browser):
        std_email = "testemail@example.com"
        std_pass  = "testpass"
        browser.get("https://automationexercise.com")
        lp = LoginPage(browser)
        lp.login(std_email, std_pass)

        try:
            # if login succeeded, this element will appear
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as')]"))
            )
        except TimeoutException:
            # LOGIN FAILED → automate registration
            rp = RegisterPage(browser)
            name      = "AutoUser"
            timestamp = int(time.time())
            email     = f"autouser{timestamp}@example.com"
            password  = "Test@1234"

            rp.signup(name, email)
            rp.fill_account_info(
                password,
                first_name=name,
                last_name="Tester",
                address="123 Main St",
                country="United States",
                state="CA",
                city="San Francisco",
                zipcode="94105",
                mobile="1234567890"
            )

            # Complete registration
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Continue"))
            ).click()

            # Log out so we can re‑test login
            browser.find_element(By.LINK_TEXT, "Logout").click()

            # Back to login form
            browser.find_element(By.LINK_TEXT, "Signup / Login").click()
            lp.login(email, password)

            # now we should see the “Logged in as” banner
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as')]"))
            )

        # final assertion: user is logged in
        assert browser.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").is_displayed()
        log_result("test_login_or_register", "PASS")

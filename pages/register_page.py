from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_name    = (By.XPATH, "//input[@data-qa='signup-name']")
        self.signup_email   = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_button  = (By.XPATH, "//button[@data-qa='signup-button']")

    def signup(self, name: str, email: str):
        self.driver.find_element(*self.signup_name).send_keys(name)
        self.driver.find_element(*self.signup_email).send_keys(email)
        self.driver.find_element(*self.signup_button).click()
        # wait for the password field on “Enter Account Information”
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )

    def fill_account_info(
        self,
        password: str,
        first_name: str,
        last_name: str,
        address: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile: str
    ):
        # Title
        self.driver.find_element(By.ID, "id_gender1").click()
        # Password
        self.driver.find_element(By.ID, "password").send_keys(password)
        # DOB
        Select(self.driver.find_element(By.ID, "days")).select_by_value("1")
        Select(self.driver.find_element(By.ID, "months")).select_by_value("1")
        Select(self.driver.find_element(By.ID, "years")).select_by_value("2000")
        # Name & Address
        self.driver.find_element(By.ID, "first_name").send_keys(first_name)
        self.driver.find_element(By.ID, "last_name").send_keys(last_name)
        self.driver.find_element(By.ID, "address1").send_keys(address)
        # Country dropdown
        Select(self.driver.find_element(By.ID, "country")).select_by_visible_text(country)
        self.driver.find_element(By.ID, "state").send_keys(state)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "zipcode").send_keys(zipcode)
        self.driver.find_element(By.ID, "mobile_number").send_keys(mobile)
        # Submit
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()

        # ← NEW: wait for the “Continue” link to appear (safer than the H2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Continue"))
        )

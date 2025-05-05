from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_link      = (By.LINK_TEXT,        "Signup / Login")
        self.email_input     = (By.XPATH,            "//input[@data-qa='login-email']")
        self.password_input  = (By.XPATH,            "//input[@data-qa='login-password']")
        self.login_button    = (By.XPATH,            "//button[@data-qa='login-button']")

    def login(self, email, password):
        self.driver.find_element(*self.login_link).click()
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

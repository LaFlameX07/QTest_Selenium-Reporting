from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    search_input = (By.ID, "search_input")  # or correct locator
    search_button = (By.ID, "search_button")

    def search(self, term):
        self.driver.find_element(*self.search_input).send_keys(term)
        self.driver.find_element(*self.search_button).click()

    def get_results_count(self):
        return len(self.driver.find_elements(*self.results))

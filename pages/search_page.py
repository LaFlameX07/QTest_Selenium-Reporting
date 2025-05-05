from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver        = driver
        self.search_input  = (By.ID,    "search_product")
        self.search_button = (By.ID,    "submit_search")
        self.results       = (By.CLASS_NAME, "productinfo")

    def search(self, term):
        self.driver.find_element(*self.search_input).send_keys(term)
        self.driver.find_element(*self.search_button).click()

    def get_results_count(self):
        return len(self.driver.find_elements(*self.results))

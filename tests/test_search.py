import pytest
from pages.search_page import SearchPage
from utils.logger import log_result

@pytest.mark.usefixtures("browser")
class TestSearch:
    def test_product_search(self, browser):
        try:
            browser.get("https://automationexercise.com")
            sp = SearchPage(browser)
            sp.search("dress")

            count = sp.get_results_count()
            assert count > 0
            log_result("test_product_search", "PASS", f"{count} items found")
        except Exception as e:
            log_result("test_product_search", "FAIL", str(e))
            browser.save_screenshot("screenshots/test_product_search.png")
            raise

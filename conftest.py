import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

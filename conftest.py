import pytest
from selenium import webdriver
import test_data


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(test_data.Urls.main_url)
    yield driver
    driver.quit()
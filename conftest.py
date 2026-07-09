import pytest
from selenium import webdriver
import helpers


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(helpers.Urls.main_url)
    yield driver
    driver.quit()
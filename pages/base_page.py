from locators import base_page_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по логотипу "Яндекс"')
    def click_on_yandex_logo(self):
        self.driver.find_element(*base_page_locators.yandex_logo).click()

    @allure.step('Клик по логотипу "Самокат"')
    def click_on_scooter_logo(self):
        self.driver.find_element(*base_page_locators.scooter_logo).click()

    @allure.step('Клик по кнопке "Заказать" в шапке страницы')
    def click_on_order_button(self):
        self.driver.find_element(*base_page_locators.order_header_button).click()

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, helpers.Timeouts.base_timeout).until(EC.visibility_of_element_located((locator)))
    
    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ввод текста в инпутное поле')
    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
    
    @allure.step('')
    def check_visibility(self, locator):
        return self.driver.find_element(*locator).is_displayed()
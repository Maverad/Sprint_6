from locators import base_page_locators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data
import allure


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Клик по логотипу "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_element(base_page_locators.yandex_logo)

    @allure.step('Клик по логотипу "Самокат"')
    def click_on_scooter_logo(self):
        self.click_on_element(base_page_locators.scooter_logo)

    @allure.step('Клик по кнопке "Заказать" в шапке страницы')
    def click_on_order_button(self):
        self.click_on_element(base_page_locators.order_header_button)

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((locator)))

    @allure.step('Ожидание открытия страницы яндекса')
    def wait_for_yandex_page(self):
        return self.wait_for_element(base_page_locators.yandex_page_search_input)
    
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
    
    def check_visibility(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def wait_for_already_known_element(self, element):
        WebDriverWait(self.driver, test_data.Timeouts.base_timeout).until(EC.visibility_of(element))

    def get_current_url(self):
        return self.driver.current_url
    
    def switch_window(self, window):
        self.driver.switch_to.window(self.driver.window_handles[window])

    def get_text_of_the_element(self, locator):
        return self.find_element(locator).text

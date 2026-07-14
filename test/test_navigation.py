from pages.main_page import MainPage 
from locators import base_page_locators, main_page_locators
import allure


class TestNavigation:
    
    @allure.title('Переход по кнопке "Самокат"')
    def test_navigation_main_page_scooter_logo(self, driver):
        main = MainPage(driver)
        main.click_on_order_button()
        main.click_on_scooter_logo()

        assert main.check_visibility(main_page_locators.home_header)

    @allure.title('Переход по кнопке "Yandex"')
    def test_navigation_main_page_yandex_logo(self, driver):
        main = MainPage(driver)
        main.click_on_yandex_logo()
        driver.switch_to.window(driver.window_handles[-1])
        main.wait_for_element(base_page_locators.yandex_page_search_input)

        assert 'ya.ru' in driver.current_url


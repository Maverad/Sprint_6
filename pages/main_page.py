from pages.base_page import BasePage
from locators import main_page_locators
import allure


class MainPage(BasePage):
    
    @allure.step('Ожидание главного заголовка на главной странице')
    def wait_for_main_header(self):
        self.wait_for_element(main_page_locators.home_header)

    @allure.step('Скролл до большой кнопки заказа на главной странице')
    def scroll_to_big_order_button(self):
        self.scroll_to_element(main_page_locators.order_big_button)

    @allure.step('Скролл до вопросов о важном')
    def scroll_to_main_questions(self):
        self.scroll_to_element(main_page_locators.questions[0])

    @allure.step('Клик на принятие кук')
    def accept_all_cookie(self):
        self.click_on_element(main_page_locators.accept_cookie_button)


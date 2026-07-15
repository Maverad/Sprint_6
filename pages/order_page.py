from locators import order_locators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Ожидание экрана заказа самоката')
    def wait_for_order_screen(self):
        self.wait_for_element(order_locators.order_name_input)

    @allure.step('Ожидание экрана деталей заказа')
    def wait_for_last_order_screen(self):
        self.wait_for_element(order_locators.order_complete_button)

    @allure.step('Ожидание экрана статуса заказа')
    def wait_for_last_status_screen(self):
        self.wait_for_element(order_locators.order_status_button)

    @allure.step('Ожидание экрана подтверждения заказа')
    def wait_for_confirmation_screen(self):
        self.wait_for_element(order_locators.order_modal_confirmation_header)

    @allure.step('Заполнение поля "Имя"')
    def fill_name_input(self, name):
        self.input_text(order_locators.order_name_input, name)

    @allure.step('Заполнение поля "Фамилия"')
    def fill_secondname_input(self, second_name):
        self.input_text(order_locators.order_second_name_input, second_name)

    @allure.step('Заполнение поля "Адрес"')
    def fill_address_input(self, address):
        self.input_text(order_locators.order_address_input, address)

    @allure.step('Выбор станции метро')
    def choose_metro_station(self):
        self.click_on_element(order_locators.order_metro_station_input)
        self.scroll_to_element(order_locators.order_metro_station_choose)
        self.click_on_element(order_locators.order_metro_station_choose)

    @allure.step('Заполнение поля "Телефон"')
    def fill_number_imput(self, number):
        self.input_text(order_locators.order_number_input, number)

    @allure.step('Клик на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_on_element(order_locators.order_next_button)

    @allure.step('Заполнение даты доставки')
    def fill_delivery_date(self):
        self.click_on_element(order_locators.order_delivery_date_calendar_open)
        self.wait_for_element(order_locators.order_delivery_date_choose)
        self.click_on_element(order_locators.order_delivery_date_choose)

    @allure.step('Заполнение срока аренды')
    def fill_hire_time(self):
        self.click_on_element(order_locators.order_hire_time_dropdown)
        self.wait_for_element(order_locators.order_hire_time_choose)
        self.click_on_element(order_locators.order_hire_time_choose)

    @allure.step('Выбор цвета самоката (черный)')
    def fill_scooter_color_black(self):
        self.click_on_element(order_locators.order_black_scooter_checkbox)

    @allure.step('Выбор цвета самоката (серый)')
    def fill_scooter_color_grey(self):
        self.click_on_element(order_locators.order_grey_scooter_checkbox)

    @allure.step('Заполнение комментария для курьера')
    def fill_comment_imput(self, text):
        self.input_text(order_locators.order_comment, text)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_complete_button(self):
        self.click_on_element(order_locators.order_complete_button)

    @allure.step('Клик на кнопку "Да" в окне подтверждения')
    def click_on_yes_button(self):
        self.click_on_element(order_locators.order_yes_button)

    @allure.step('Заполнение формы заказа')
    def fill_entire_form(self, name, second_name, address, number):
        self.fill_name_input(name)
        self.fill_secondname_input(second_name)
        self.fill_address_input(address)
        self.choose_metro_station()
        self.fill_number_imput(number)
    
    @allure.step('Заполнение деталей аренды')
    def fill_entire_hire_form(self, text):
        self.fill_delivery_date()
        self.fill_hire_time()
        self.fill_scooter_color_black()
        self.fill_comment_imput(text)
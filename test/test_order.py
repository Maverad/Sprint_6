import helpers
from pages.order_page import OrderPage
from helpers import OrderData as od
from locators import order_locators, main_page_locators
import pytest
import allure


class TestOrder:

    @allure.title('Заказ самоката через кнопку заказа в шапке')
    @pytest.mark.parametrize('name, second_name, address, number', list(zip(od.name, od.second_name, od.address, od.number)))
    def test_positive_order_from_header(self, driver, name, second_name, address, number):
        order = OrderPage(driver)
        order.click_on_order_button()
        order.wait_for_order_screen()
        order.fill_entire_form(name=name, second_name=second_name, address=address,number=number)
        order.click_on_next_button()
        order.wait_for_last_order_screen()
        order.fill_entire_hire_form(text=helpers.OrderData.text_for_comment)
        order.click_on_complete_button()
        order.wait_for_confirmation_screen()
        order.click_on_yes_button()
        order.wait_for_last_status_screen()

        assert order.check_visibility(order_locators.order_status_button)
        assert order.check_visibility(order_locators.order_status_header)
       
    @allure.title('Заказ самоката через большую кнопку заказа')
    @pytest.mark.parametrize('name, second_name, address, number', list(zip(od.name, od.second_name, od.address, od.number)))
    def test_positive_order_from_big_button(self, driver, name, second_name, address, number):
        order = OrderPage(driver)
        order.scroll_to_element(main_page_locators.order_big_button)
        order.click_on_element(main_page_locators.order_big_button)
        order.wait_for_order_screen()
        order.fill_entire_form(name=name, second_name=second_name, address=address,number=number)
        order.click_on_next_button()
        order.wait_for_last_order_screen()
        order.fill_entire_hire_form(text=od.text_for_comment)
        order.click_on_complete_button()
        order.wait_for_confirmation_screen()
        order.click_on_yes_button()
        order.wait_for_last_status_screen()
    
        assert order.check_visibility(order_locators.order_status_button)
        assert order.check_visibility(order_locators.order_status_header)
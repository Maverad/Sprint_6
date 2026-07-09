from selenium.webdriver.common.by import By


#first form
order_name_input = (By.XPATH, ".//input[@placeholder='* Имя']")
order_second_name_input = (By.XPATH, ".//input[@placeholder='* Фамилия']")
order_address_input = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
order_number_input = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
order_next_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
order_metro_station_input = (By.XPATH, ".//input[@placeholder='* Станция метро']")
order_metro_station_choose = (By.XPATH, ".//div[@class='select-search__select']/ul/li/button[@value=24]")

#second form - hire details
order_delivery_date_calendar_open = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
order_delivery_date_choose = (By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--016']")
order_hire_time_dropdown = (By.XPATH, ".//span[@class='Dropdown-arrow']")
order_hire_time_choose = (By.XPATH, ".//div[@class='Dropdown-option' and text()='трое суток']")
order_black_scooter_checkbox = (By.XPATH, ".//input[@id='black']")
order_grey_scooter_checkbox = (By.XPATH, ".//input[@id='grey']")
order_comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
order_back_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Назад']")
order_complete_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

#confirmation modal screen
order_modal_confirmation_header = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']")
order_yes_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
order_no_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Нет']")

#success modal screen
order_status_button = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button")
order_status_header = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']/div[@class='Order_ModalHeader__3FDaJ']")
from selenium.webdriver.common.by import By


order_big_button = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button") 
questions = (By.CLASS_NAME, "accordion__item")
answers = (By.XPATH, ".//div[@class='accordion__panel']/p")
questions_first_question = (By.XPATH, "(.//div[@class='accordion__item'])[1]")
home_header = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
accept_cookie_button = (By.XPATH, ".//button[@id='rcc-confirm-button']")
from selenium.webdriver.common.by import By


order_big_button = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button") 
questions = (By.CLASS_NAME, "accordion__item")
answers = [
    (By.XPATH, "(.//div[@class='accordion__panel']/p)[1]"),
    (By.XPATH, "(.//div[@class='accordion__panel']/p)[2]"),
    (By.XPATH, "(.//div[@class='accordion__panel']/p)[3]"),
    (By.XPATH, "(.//div[@class='accordion__panel']/p)[4]"),
    (By.XPATH, "(.//div[@class='accordion__panel']/p)[5]"),
    (By.XPATH, "(.//div[@class='accordion__panel']/p)[6]"),
    (By.XPATH, "(.//div[@class='accordion__panel']/p)[7]")
    ]
questions = [
    (By.XPATH, "(.//div[@class='accordion__item'][1])"),
    (By.XPATH, "(.//div[@class='accordion__item'][2])"),
    (By.XPATH, "(.//div[@class='accordion__item'][3])"),
    (By.XPATH, "(.//div[@class='accordion__item'][4])"),
    (By.XPATH, "(.//div[@class='accordion__item'][5])"),
    (By.XPATH, "(.//div[@class='accordion__item'][6])"),
    (By.XPATH, "(.//div[@class='accordion__item'][7])")
]
questions_first_question = (By.XPATH, "(.//div[@class='accordion__item'])[1]")
home_header = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
accept_cookie_button = (By.XPATH, ".//button[@id='rcc-confirm-button']")
from pages.main_page import MainPage
from locators import main_page_locators
from test_data import Questions_data as qd
import allure


class TestQuestions:
    
    @allure.title('Проверка корректности вопросов')
    def test_questions_text(self, driver):
        questions = MainPage(driver)
        questions.scroll_to_main_questions()
        elements = questions.find_elements(main_page_locators.questions)
        counter = 0
        for i in elements:
            assert i.text == qd.questions_data[counter]
            counter += 1
    
    @allure.title('Проверка корректности ответов к вопросам')
    def test_answers_for_questions(self, driver):
        answers = MainPage(driver)
        answers.scroll_to_main_questions()
        answers.accept_all_cookie()
        elements_answers = answers.find_elements(main_page_locators.answers)
        elements_questions = answers.find_elements(main_page_locators.questions)
        counter = 0
        for i in elements_answers:
            qs = elements_questions[counter]
            qs.click()
            answers.wait_for_already_known_element(i)
            assert i.text == qd.answers_data[counter]
            counter += 1


from pages.main_page import MainPage
from locators import main_page_locators
from test_data import Questions_data as qd
import allure
import pytest

class TestQuestions:
    
    @pytest.mark.parametrize('answer_locator, expected_answer, question_locator', list(zip(main_page_locators.answers, qd.answers_data.values(), main_page_locators.questions)))
    @allure.title('Проверка корректности ответов к вопросам')
    def test_answer_for_questions(self, driver, answer_locator, expected_answer, question_locator):
        answers = MainPage(driver)
        answers.scroll_to_main_questions()
        answers.accept_all_cookie()
        answers.click_on_element(question_locator)
        answers.wait_for_element(answer_locator)

        assert answers.check_visibility(answer_locator)
        assert answers.get_text_of_the_element(answer_locator) == expected_answer






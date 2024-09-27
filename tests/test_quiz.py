import time
import pytest
from pages.quiz_page import QuizPage
from utils.driver import init_driver
@pytest.fixture(scope="function")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()

def test_verify_header_of_start_quiz(driver):
    """verify header text on start quiz screen"""
    quiz_page = QuizPage(driver)
    expected_header_text = "Learn Flutter the fun way!"
    actual_header_text = quiz_page.get_header_text()
    print("Actual Header Text:", actual_header_text)

    assert expected_header_text == actual_header_text, f"Expected header text '{expected_header_text}' but got '{actual_header_text}'"

def test_start_button_visibility(driver):
    """Verify that the 'Start Quiz' button is disabled if the quiz is already in progress."""
    quiz_page = QuizPage(driver)
    assert quiz_page.is_start_button_present(), "'Start Quiz' button is not visible before starting the quiz."
    quiz_page.start_quiz()
    assert not quiz_page.is_start_button_present(), "'Start Quiz' button is still visible after starting the quiz."


def test_start_quiz_button_navigation(driver):
    """Verify that clicking the 'Start Quiz' button navigates to the first question screen."""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    assert quiz_page.is_question_displayed(), "Failed to navigate to the first question screen."

def test_answer_first_question_randomly(driver):
    """answering first question by selecting any option at random"""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    current_question_text = quiz_page.get_current_question_text()
    quiz_page.answer_a_question()
    print(current_question_text)
    new_question_text = quiz_page.get_current_question_text()
    print(new_question_text)
    assert current_question_text != new_question_text, "The question did not change after answering."

def test_answer_all_questions_randomly(driver):
    """answering all questions randomly"""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    while not quiz_page.is_result_page_displayed():
        quiz_page.answer_a_question()
    assert quiz_page.is_result_page_displayed(), "result page is not displayed"

def test_correct_score_display(driver):
    """Verify that the correct score is displayed on the results screen."""
    quiz_page = QuizPage(driver)
    test_answer_all_questions_randomly(driver)
    correct_count=quiz_page.correct_score()
    print(correct_count)
    Expected= f"You answered {correct_count} out of 6 questions correctly!"
    actual=quiz_page.get_result_score_text()
    assert  Expected == actual, f"Expected header text '{Expected}' but got '{actual}'"

def test_all_correct_answer_and_score(driver):
    """testing all the questions with correct option and verify score"""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    quiz_page.all_answers_correct()
    correct_count = quiz_page.correct_score()
    print(correct_count)
    Expected = f"You answered {correct_count} out of 6 questions correctly!"
    actual = quiz_page.get_result_score_text()
    assert Expected == actual, f"Expected header text '{Expected}' but got '{actual}'"

def test_start_quiz_and_minimize(driver):
    """Test answering some quiz questions, minimizing the app, and reopening."""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    current_question_text = quiz_page.get_current_question_text()
    print(current_question_text)
    quiz_page.minimize_app(5)
    new_question_text = quiz_page.get_current_question_text()
    print(new_question_text)
    assert current_question_text == new_question_text, "The question did not change after minimising."

def test_app_crash_handling(driver):
    """Simulate an app crash and verify recovery."""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    quiz_page.crash_app_crash()
    time.sleep(5)
    assert quiz_page.get_start_quiz_button().is_displayed(), "App did not recover from crash."

def test_restart_button_takes_to_start_quiz(driver):
    """verify restart button"""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    while not quiz_page.is_result_page_displayed():
        quiz_page.answer_a_question()
    assert quiz_page.is_result_page_displayed(), "result page is not displayed"
    quiz_page.click_restart()
    assert quiz_page.is_start_button_present(), "'Start Quiz' button is not visible before starting the quiz."

def test_start_quiz_and_press_back_button(driver):
    """starting quiz and press back button and check behaviour"""
    quiz_page = QuizPage(driver)
    quiz_page.start_quiz()
    quiz_page.navigate_back_and_launch()
    time.sleep(5)
    assert quiz_page.is_start_button_present(), "'Start Quiz' button is not visible before starting the quiz."

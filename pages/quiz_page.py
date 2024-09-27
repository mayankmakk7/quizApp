import random
import json
import os
from pages.base_page import BasePage
from locators.quiz_locators import QuizLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def read_json():
    current_file_directory = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(current_file_directory,'..','resources', 'quiz_repo.json'))
    print(file_path)
    with open(file_path, 'r') as json_file:
        try:
            data = json.load(json_file)
        except Exception as e:
            print(e)
    return data


class QuizPage(BasePage):
    def get_header_locator(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(QuizLocators.quiz_header_text)
        )

    def get_start_quiz_button(self):
        return self.driver.find_element(*QuizLocators.start_quiz_button)

    def start_quiz(self):
        self.click(*QuizLocators.start_quiz_button)

    def get_answer_buttons(self):
        """Find all answer buttons dynamically."""
        return self.driver.find_elements(*QuizLocators.answers_options)

    def answer_a_question(self):
        answer_buttons = self.get_answer_buttons()
        random_answer_index = random.randint(1, 4) - 1  # Randomly choose between 1 and 4, convert to 0-based index
        answer_buttons[random_answer_index].click()

    def is_question_displayed(self):
        return any(self.is_element_present(*locator) for locator in QuizLocators.question_locators)

    def is_start_button_present(self):
        """Check if the 'Start Quiz' button is present in the DOM."""
        try:
            self.find(*QuizLocators.start_quiz_button)
            return True
        except NoSuchElementException:
            return False

    def get_header_text(self):
        return self.get_text(*QuizLocators.quiz_header_text)

    def get_current_question_text(self):
        for ques in QuizLocators.question_locators:
            try:
                return self.get_text(*ques)
            except Exception as e:
                continue
        return None

    def is_result_page_displayed(self):
        try:
            self.find(*QuizLocators.result_page_text)
            return True
        except NoSuchElementException:
            return False

    def correct_score(self):
        count = 0
        json_dict = read_json()
        for value in json_dict.values():
            num = self.driver.find_elements(By.XPATH, f"//android.view.View[@content-desc='{value}']")
            if len(num) ==0:
                self.driver.swipe(150, 1500, 150, 200, 500)
                num = self.driver.find_elements(By.XPATH, f"//android.view.View[@content-desc='{value}']")

            if len(num) > 1:
                count += 1
        return count

    def get_result_score_text(self):
        return self.get_text(*QuizLocators.result_page_text)

    def all_answers_correct(self):
        json_dict = read_json()
        for value in json_dict.values():
            loc = self.driver.find_element(By.XPATH, f"//android.widget.Button[@content-desc='{value}']")
            loc.click()

    def crash_app_crash(self):
        super().app_crash()

    def click_restart(self):
        self.click(*QuizLocators.restart_button)
    def click_app(self):
        self.click(*QuizLocators.app_loc)
    def navigate_back_and_launch(self):
        """Navigate back to the previous screen using explicit wait."""
        self.back()
        self.click_app()
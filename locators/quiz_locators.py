from selenium.webdriver.common.by import By

class QuizLocators:

    quiz_header_text=(By.XPATH,"//android.view.View[@content-desc='Learn Flutter the fun way!']")
    start_quiz_button = (By.XPATH, "//android.widget.Button[@content-desc='Start Quiz']")
    answers_options = (By.CLASS_NAME , 'android.widget.Button')
    question_locators = [
        (By.XPATH, '//android.view.View[@content-desc="What are the main building blocks of Flutter UIs?"]'),
        (By.XPATH, '//android.view.View[@content-desc="How are Flutter UIs built?"]'),
    ]
    restart_button=(By.XPATH,'//android.widget.Button[@content-desc="Restart"]')
    result_page_text=(By.XPATH,"//android.view.View[contains(@content-desc,'questions correctly!')]")
    app_loc=(By.XPATH,"//android.widget.TextView[@content-desc='Predicted app: quiz_app']")
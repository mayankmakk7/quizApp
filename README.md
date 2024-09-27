Author : Mayank

**Appium Test Automation Framework for a Quiz App
**Table of Contents:
Introduction
Framework Structure
Pre-requisites
Setup Instructions
How to Run Tests
Running Tests with Reports
Writing New Tests
testcases
future scope

**Introduction**
This is an automated test framework for a Quiz App built using Appium and Python. The framework follows the Page Object Model (POM) pattern for clean and maintainable test code. It uses pytest as the test runner and supports reporting through pytest-html.

**Framework Structure
**The project is organized into the following directories:


appium_framework/
│
├── tests/                     # Test scripts
│   ├── test_quiz.py      # all Testcases for  quiz app
│   
│
├── pages/                     # Page Object Model classes
│   ├── base_page.py             # Base class for all pages
│   ├── quiz_page.py             # Page actions for quiz-related functionality
│
├── locators/                  # Locator classes
│   ├── quiz_locators.py        # Locators for quiz page elements
│
├── utils/                     # Utility functions
│   ├── driver.py               # Driver setup for Appium
│
├── reports/                   # Test reports (pytest-html)
│
├── resources/                 # Additional resources (APK, configs)
│   ├── app-release.apk             # APK file for the app under test
|   ├── quiz_repo.json         #considering this is source for questions and answers
│
├── requirements.txt           # Python dependencies
│
├── pytest.ini                 # Pytest configuration file
│
└── conftest.py                # Pytest setup hooks
**Pre-requisites
**Before setting up the project, ensure you have the following installed on your machine:

Java Development Kit (JDK): Ensure that the JAVA_HOME environment variable is correctly set.
Appium: Installed via npm or use Appium Desktop.
Android SDK: For running the Android emulator.
Python 3.x: Install Python 3.7 or later.
Node.js: Required for Appium.
Setup Instructions
1. Clone the Repository
   
git clone https://github.com/mayankmakk7/quizApp.git
cd quizApp
3. Install Dependencies
Make sure you have Python and pip installed, then run the following command to install all required dependencies:

pip install -r requirements.txt
3. Install and Start Appium
Make sure Appium is installed:

npm install -g appium
Start the Appium server in a separate terminal:

appium --base-path /wd/hub
4. Configure Android Emulator or Real Device
If you are using an Android emulator, ensure it's running. You can start an emulator using Android Studio or the command line.
If you're using a real Android device, enable USB Debugging on the device and connect it to your system.
and change the configuration as required in driver.py file

**How to Run Tests
**1. Run All Tests
To run all the tests, simply use:
pytest

**Running Tests with Reports
**1. Generate an HTML Report
To generate a basic HTML report after running the tests, use the following command:

pytest --html=reports/report.html

**Writing New Tests
**To add a new test case, follow these steps:

Create a New Test File: Add a new file under the tests/ directory.
Use Page Object Model: Add actions to the corresponding page class (e.g., QuizPage).
Add Locators: Add new locators to the locators/quiz_locators.py file if required.
Write Test Logic: Write the test logic using pytest in your test file.

**Testcases**
  1.verify header text on start quiz view
  2.verify visiblity of start quiz vutton
  3.verify quiz gets started once clicked
  4.verify answering a question with random option
  5.verify answering all questions randomly
  6.verify quiz score display
  7.verify selecting all correct answers and score
  8.verify behaviour when quiz started and app is minimised and open again
  9.verify if quiz started and app got crashed(simulating crash has been done through code)
  10.verify restart button takes to start of quiz
  11.verify behaviour when quiz started and user pressed back button
  12.verify behaviour if network is down
  13.verify correct answer shows with green color -- not automated since release apk do not expose all the ui components
  14.verify wrong answers shows with orange color -- not automated since release apk do not expose all the ui components

 **Future Score**
 Jenkins Integration to run the tests periodically in a schedule.


Fork the repository.
Create a new feature branch.
Make your changes and submit a pull request.


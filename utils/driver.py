from appium import webdriver
from appium.options.android import UiAutomator2Options
import os


def init_driver():
    current_file_directory = os.path.dirname(__file__)
    apk_path = os.path.join(current_file_directory, '..', 'resources', 'app-release.apk')
    print(apk_path)
    desired_caps =  {
        "platformName": "Android",
        "platformVersion": "15",
        "deviceName": "emulator-5554",
        "app": apk_path,
        "appPackage": "com.example.quiz_app",
        "appActivity": "com.example.quiz_app.MainActivity",
        "automationName": "UiAutomator2",
        "newCommandTimeout": 300
        # "noReset": True
    }
    print(type(desired_caps))
    try:
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        print("Initializing Appium driver...")
        driver = webdriver.Remote("http://localhost:4723/wd/hub",options=capabilities_options)
        print("Driver initialized successfully.")
        return driver
    except Exception as e:
        print(f"Error initializing driver: {str(e)}")
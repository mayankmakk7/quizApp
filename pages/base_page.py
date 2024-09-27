import time
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        self.find(by, locator).click()

    def is_element_present(self, by, locator):
        try:
            self.find(by, locator)
            return True
        except:
            return False

    def get_text(self, by, locator):
        """Get the text of the element using either 'text' or 'content-desc'."""
        element = self.find(by, locator)
        text = element.get_attribute("text")  # Standard text attribute
        if not text:
            text = element.get_attribute("contentDescription")  # Fallback to content-desc
        return text
    def start_app(self):
        """Starts the app using the driver."""
        if not self.driver.session_id:
            self.driver.start_session(desired_capabilities=self.driver.desired_capabilities)
        else:
            self.driver.launch_app()

    def get_attribute(self, by, locator, attribute_name):
        return self.find(by, locator).get_attribute(attribute_name)

    def minimize_app(self, duration=5):
        """Minimizes the app and brings it back to foreground after the duration."""
        self.driver.background_app(duration)
        time.sleep(5)

    def back(self):
        """Navigates back to the previous screen using device back button."""
        self.driver.back()
    def close_app(self):
        self.driver.quit()
    def app_crash(self):
        """Simulates an app crash by terminating and relaunching the app."""
        app_package = self.driver.current_package
        self.driver.terminate_app(app_package)
        time.sleep(2)
        self.driver.activate_app(app_package)

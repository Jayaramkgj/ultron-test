from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Loginpage():
    def __init__(self,driver):
        self.driver = driver

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_name("username")
        except NoSuchElementException:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name("pwd")
        except NoSuchElementException:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='submit']")
        except NoSuchElementException:
            return None

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(self.driver,30)
        wait.until_expected_condition_visibility_of(self.driver.find_element_by_name("loginForm"))
        





import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# def screenshot_on_failure(func):
#     def wrapper(self, *arg, **kw):
#         try:
#             return func(self, *arg, **kw)
#         except AssertionError:
#             attach_screenshot_to_report(self.driver)
#     return wrapper

class Driver:
    @staticmethod
    def instantiate_driver():
        print("Initializing Driver")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver


class Wrapper:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.wait = WebDriverWait(self.driver, 20)
        self.logger = logging.getLogger(__name__)

    def element(self, locator):
        element_located = self.wait.until(ec.visibility_of_element_located(locator))
        return element_located

    def click(self, locator=None):
        element_located = self.element(locator)
        element_located.click()
        return element_located

    def send_keys(self, locator, text=''):
        element_located = self.element(locator)
        element_located.clear()
        element_located.send_keys(text)
        return element_located

    def assert_text(self, locator, text):
        if type(locator) == str:
            assert locator == text
        else:
            assert self.element(locator).text == text

    def is_displayed(self, locator):
        element_located = self.wait.until(ec.presence_of_element_located(locator))
        return element_located.is_displayed()



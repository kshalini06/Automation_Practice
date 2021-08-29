import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from resources.locators import Locators
from selenium.webdriver.support import expected_conditions as ec

from utilities.selenium_utility import Wrapper


class LoginPage(Wrapper):
    def __init__(self, driver):
        super().__init__(driver)

        self.create_account = Locators.create_account
        self.already_registered = Locators.already_registered
        self.email_create = Locators.email_create
        self.submit_create = Locators.submit_create
        self.enter_email = Locators.enter_email
        self.password = Locators.password
        self.forgot_password = Locators.forgot_password
        self.submit_login = Locators.submit_login
        self.incorrect_email_create = Locators.incorrect_email_create
        self.email_create_error = Locators.email_create_error
        self.view_account = Locators.view_account
        self.sign_out = Locators.sign_out
        self.login_failed = Locators.login_failed

    def enter_email_for_registration(self, email_id):
        self.send_keys(self.email_create, email_id)

    def enter_email_for_login(self, email_id):
        self.send_keys(self.enter_email, email_id)

    def enter_password_for_login(self, password):
        self.send_keys(self.password, password)

    def click_submit_create(self):
        self.click(self.submit_create)

    @allure.step("Logging in")
    def click_submit_login(self):
        self.click(self.submit_login)

    def click_forgot_password(self):
        self.click(self.forgot_password)

    @allure.step("Signing out")
    def sign_out_from_account(self):
        self.click(self.sign_out)

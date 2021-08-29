import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from resources.locators import Locators
from selenium.webdriver.support import expected_conditions as ec

from utilities.selenium_utility import Wrapper


class RegistrationPage(Wrapper):
    def __init__(self, driver):
        super().__init__(driver)

        self.your_personal_info = Locators.your_personal_info
        self.title_mr = Locators.title_mr
        self.title_mrs = Locators.title_mrs
        self.customer_firstname = Locators.customer_firstname
        self.customer_lastname = Locators.customer_lastname
        self.customer_email = Locators.customer_email
        self.customer_password = Locators.customer_password
        self.dob_select_days = Locators.dob_select_days
        self.dob_select_months = Locators.dob_select_months
        self.dob_select_years = Locators.dob_select_years
        self.checkbox_newsletter = Locators.checkbox_newsletter
        self.checkbox_special_offers = Locators.checkbox_special_offers
        self.label_your_address = Locators.label_your_address
        self.your_add_firstname = Locators.your_add_firstname
        self.your_add_lastname = Locators.your_add_lastname
        self.your_add_company = Locators.your_add_company
        self.your_add_addline1 = Locators.your_add_addline1
        self.your_add_addline2 = Locators.your_add_addline2
        self.your_add_city = Locators.your_add_city
        self.your_add_state_dropdown = Locators.your_add_state_dropdown
        self.your_add_postcode = Locators.your_add_postcode
        self.your_add_country_dropdown = Locators.your_add_country_dropdown
        self.your_add_additional_info = Locators.your_add_additional_info
        self.your_add_home_phn = Locators.your_add_home_phn
        self.your_add_mobile_phn = Locators.your_add_mobile_phn
        self.your_add_add_alias = Locators.your_add_add_alias
        self.register_button = Locators.register_button

    def select_title(self, title):
        if title == 'Mr':
            self.click(self.title_mr)
        else:
            self.click(self.title_mrs)
        time.sleep(2)

    def enter_firstname(self, firstname):
        self.send_keys(self.customer_firstname, firstname)
        time.sleep(2)

    def enter_lastname(self, lastname):
        self.send_keys(self.customer_lastname, lastname)
        time.sleep(2)

    def enter_password(self, password):
        self.send_keys(self.customer_password, password)
        time.sleep(2)

    def enter_add_firstname(self, firstname):
        self.send_keys(self.your_add_firstname, firstname)
        time.sleep(2)

    def enter_add_lastname(self, lastname):
        self.send_keys(self.your_add_lastname, lastname)
        time.sleep(2)

    def enter_add_address(self, address):
        self.send_keys(self.your_add_addline1, address)
        time.sleep(2)

    def enter_add_city(self, city):
        self.send_keys(self.your_add_city, city)
        time.sleep(2)

    def select_state(self, state):
        sel = Select(self.wait.until(ec.presence_of_element_located(self.your_add_state_dropdown)))
        sel.select_by_visible_text(state)
        time.sleep(2)

    def enter_postal_code(self, pin):
        self.send_keys(self.your_add_postcode, pin)
        time.sleep(2)

    def select_country(self, country):
        sel = Select(self.wait.until(ec.presence_of_element_located(self.your_add_country_dropdown)))
        sel.select_by_visible_text(country)
        time.sleep(2)

    def enter_mobile_phn(self, phn):
        self.send_keys(self.your_add_mobile_phn, phn)
        time.sleep(2)

    def enter_address_alias(self, alias):
        self.send_keys(self.your_add_add_alias, alias)
        time.sleep(2)

    def click_register(self):
        self.click(self.register_button)
        time.sleep(2)

    @allure.step("Registering user")
    def register_user(self, test_data):
        self.select_title(test_data["title"])
        self.enter_firstname(test_data["firstname"])
        self.enter_lastname(test_data["lastname"])
        self.enter_password(test_data["password"])
        self.enter_add_firstname(test_data["firstname"])
        self.enter_add_lastname(test_data["lastname"])
        self.enter_add_address(test_data["addline1"])
        self.enter_add_city(test_data["city"])
        self.select_state(test_data["state"])
        self.enter_postal_code(test_data["postalcode"])
        self.select_country(test_data["country"])
        self.enter_mobile_phn(test_data["phone"])
        self.enter_address_alias(test_data["alias"])
        self.click_register()
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="Register", attachment_type=AttachmentType.PNG)


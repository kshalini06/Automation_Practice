import calendar
import time

import pytest

from conftest import driver
from utilities import data_reader
from webpages.homePage import HomePage
from webpages.loginPage import LoginPage
from webpages.registrationPage import RegistrationPage

test_data = data_reader.excel_to_dict("Test_Data/registration.xls")


@pytest.mark.registration
@pytest.mark.parametrize("test_params", test_data)
def test_registration_1(test_params, ):
    """
        Positive registration flow
    """
    home_page = HomePage(driver)
    home_page.click_sign_in()
    login = LoginPage(driver)
    ts = calendar.timegm(time.gmtime())
    email = test_params["firstname"]+str(ts)+"@gmail.com"
    login.enter_email_for_registration(email)
    login.click_submit_create()
    register = RegistrationPage(driver)
    register.register_user(test_params)
    time.sleep(5)
    login.sign_out_from_account()


@pytest.mark.registration
@pytest.mark.parametrize("email, error_message", [("shahrukh@gmail.com", "An account using this email address has "
                                                                         "already been registered. Please enter a "
                                                                         "valid password or request a new one."),
                                                  ("shahrukhgmail.com", "Invalid email address.")])
def test_registration_2(email, error_message):
    """
    1. Entering a incorrect email
    2. Entering already used email
    """
    home_page = HomePage(driver)
    home_page.click_sign_in()
    login = LoginPage(driver)
    login.enter_email_for_registration(email)
    login.click_submit_create()
    login.assert_text(login.email_create_error, error_message)

import pytest

from conftest import driver
from webpages.homePage import HomePage
from webpages.loginPage import LoginPage


@pytest.mark.login
def test_login():
    """
    SuccessfulLogin
    """
    home_page = HomePage(driver)
    home_page.click_sign_in()
    login = LoginPage(driver)
    login.enter_email_for_login("shahrukh@gmail.com")
    login.enter_password_for_login("Password@123")
    login.click_submit_login()
    login.assert_text(login.view_account, "Shahrukh Khan")
    login.sign_out_from_account()


@pytest.mark.login
@pytest.mark.parametrize("email, password, error_message", [("shahrukh@gmail.com", "Password123", "Authentication failed."),
                                                            ("salman@gmail.com", "Password123", "Authentication failed.")])
def test_login_incorrect_password(email, password, error_message):
    """
    1. Incorrect Password
    2. Email Id not registered

    """
    home_page = HomePage(driver)
    home_page.click_sign_in()
    login = LoginPage(driver)
    login.enter_email_for_login(email)
    login.enter_password_for_login(password)
    login.click_submit_login()
    login.assert_text(login.login_failed, error_message)


@pytest.mark.login
def test_login_mandatory_password():
    """
    No Password entered
    """
    home_page = HomePage(driver)
    home_page.click_sign_in()
    login = LoginPage(driver)
    login.enter_email_for_login("shahrukh@gmail.com")
    login.click_submit_login()
    login.assert_text(login.login_failed, "Password is required.")

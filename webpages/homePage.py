import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from resources.locators import Locators
from selenium.webdriver.support import expected_conditions as ec
from conftest import url
from utilities.selenium_utility import Wrapper


class HomePage(Wrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_link = Locators.sign_in_link
        self.product = Locators.product
        self.add_to_cart = Locators.add_to_cart
        self.continue_shopping = Locators.continue_shopping
        self.proceed_to_checkout = Locators.proceed_to_checkout
        self.view_cart = Locators.view_cart
        self.cart_products = Locators.cart_products
        self.driver.get(url)

    @allure.step("Clicking Sign In")
    def click_sign_in(self):
        self.click(self.sign_in_link)

    @allure.step("Add Products to cart")
    def add_product_to_cart(self, product_name):
        for name in product_name:
            prod = self.element(Locators.product(name))
            hover = ActionChains(self.driver).move_to_element(prod)
            hover.perform()
            add = self.element(Locators.add_to_cart(name))
            hover = ActionChains(self.driver).move_to_element(add)
            hover.click().perform()
            self.click(self.continue_shopping)
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="Add to cart", attachment_type=AttachmentType.PNG)

    @allure.step("Get Cart Elements")
    def get_cart_elements(self):
        return self.driver.find_elements_by_xpath(self.cart_products[1])

    @allure.step("Delete from Cart")
    def delete_from_cart(self, product_name):
        cart = self.element(self.view_cart)
        hover = ActionChains(self.driver).move_to_element(cart)
        hover.perform()
        for name in product_name:
            remove = self.element(Locators.remove_product(name))
            hover = ActionChains(self.driver).move_to_element(remove)
            hover.click().perform()
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="Delete to cart", attachment_type=AttachmentType.PNG)








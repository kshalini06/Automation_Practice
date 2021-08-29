import time

import pytest

from conftest import driver
from webpages.homePage import HomePage
from webpages.loginPage import LoginPage


@pytest.mark.cart_add_delete
def test_add_delete_to_cart():
    home_page = HomePage(driver)
    products = ["Faded Short Sleeve T-shirts", "Blouse", "Printed Dress"]
    home_page.add_product_to_cart(products)
    cart_items = home_page.get_cart_elements()
    assert len(products) == len(cart_items)
    for i in cart_items:
        assert i.get_attribute('title') in products
    remove = [products.pop(0)]
    home_page.delete_from_cart(remove)
    time.sleep(5)
    cart_items = home_page.get_cart_elements()
    assert len(products) == len(cart_items)



import pytest
import json
from utilities.selenium_utility import Driver

env_config_file = './resources/env_config.json'
driver = None
url = None


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    global driver, url
    driver = Driver.instantiate_driver()
    with open(env_config_file) as f:
        url = json.load(f)['url']


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish():
    driver.close()



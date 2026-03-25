import os
import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            path = os.path.join(os.getcwd(), "screenshots", f"{item.name}.png")
            driver.save_screenshot(path)



@pytest.fixture()
def login_page(driver):
    driver.get("https://www.saucedemo.com")
    page = LoginPage(driver)
    return page

@pytest.fixture()
def logged_in_page(login_page):
    login_page.login("standard_user","secret_sauce")
    return login_page

@pytest.fixture()
def loaded_cart(logged_in_page):
    driver = logged_in_page.driver
    inventory = InventoryPage(driver)
    inventory.add_item()
    inventory.go_to_cart()

    cart = CartPage(driver)

    return cart



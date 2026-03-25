from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.checkout_step_one_page import CheckoutStepOnePage


class CartPage(BasePage):

    checkout_btn = (By.ID,"checkout")
    cart_title = (By.CLASS_NAME,"title")

    def __init__(self, driver):

        super().__init__(driver)
        self.wait_for_page()

    def click_checkout_btn(self):
        self.element_to_be_clickable(self.checkout_btn).click()

        return CheckoutStepOnePage(self.driver)

    def wait_for_page(self):
        self.element_to_be_visible(self.cart_title)




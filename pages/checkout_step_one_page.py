from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.checkout_step_two_page import CheckoutStepTwoPage


class CheckoutStepOnePage(BasePage):

    first_name = (By.ID,"first-name")
    last_name = (By.ID,"last-name")
    postal_code = (By.ID,"postal-code")
    continue_btn = (By.ID,"continue")
    error_message = (By.CSS_SELECTOR,".error-message-container h3")

    def __init__(self,driver):

        super().__init__(driver)
        self.wait_for_page()

    def wait_for_page(self):
        self.element_to_be_visible(self.first_name)
        self.element_to_be_visible(self.last_name)
        self.element_to_be_visible(self.postal_code)
        self.element_to_be_clickable(self.continue_btn)


    def get_first_name(self):
        return self.element_to_be_visible(self.first_name).get_attribute("value")

    def get_last_name(self):
        return self.element_to_be_visible(self.last_name).get_attribute("value")

    def get_postal_code(self):
        return self.element_to_be_visible(self.postal_code).get_attribute("value")

    def enter_first_name(self,first_name):
        self.element_to_be_visible(self.first_name).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.element_to_be_visible(self.last_name).send_keys(last_name)

    def enter_postal_code(self,postal_code):
        self.element_to_be_visible(self.postal_code).send_keys(postal_code)

    def click_continue(self):
        self.element_to_be_clickable(self.continue_btn).click()

        if self.is_error_displayed():
            return self

        return CheckoutStepTwoPage(self.driver)

    def is_error_displayed(self):
        return len(
            self.driver.find_elements(*self.error_message)
        ) > 0

    def get_error_messages(self):
        return self.element_to_be_visible(self.error_message).text

    def enter_info(self,first_name,last_name,postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

        return self.click_continue()

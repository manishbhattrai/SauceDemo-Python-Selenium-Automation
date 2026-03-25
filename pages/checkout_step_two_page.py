from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CheckoutStepTwoPage(BasePage):

    overview_txt = (By.XPATH, "//span[@class='title']")
    prices = (By.XPATH, "//div[@class='inventory_item_price']")
    cancel_btn = (By.XPATH, "//button[@id='cancel']")
    finish_btn = (By.ID, "finish")

    def __init__(self,driver):
        super().__init__(driver)
        self.wait_for_page()

    def wait_for_page(self):
        self.element_to_be_visible(self.overview_txt)

    def get_prices(self):
        return self.elements_to_be_visible(self.prices).text

    def click_cancel_btn(self):
        self.element_to_be_clickable(self.cancel_btn).click()
        WebDriverWait(self.driver, 10).until(lambda d: "/inventory" in d.current_url)

    def click_finish_btn(self):
        self.element_to_be_clickable(self.finish_btn).click()
        WebDriverWait(self.driver, 10).until(lambda d: "checkout-complete" in d.current_url)
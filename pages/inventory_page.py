from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):

    product_link = (By.CLASS_NAME, "inventory_item_name")
    dropdown_btn = (By.CLASS_NAME, "product_sort_container")
    product_prices = (By.CLASS_NAME, "inventory_item_price")
    product_names = (By.CLASS_NAME, "inventory_item_name")
    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def click_product_title(self):
        element = self.element_to_be_visible(self.product_link)
        element.click()

    def get_current_path(self):
        return self.driver.current_url

    def add_item(self):
        buttons = self.element_to_be_visible(self.add_to_cart_button)
        buttons.click()

    def go_to_cart(self):
        self.element_to_be_clickable(self.cart_icon).click()
        return CartPage(self.driver)

    def dropdown_for_ascending_alphabet(self):
        dropdown_element = self.element_to_be_clickable(self.dropdown_btn)
        select = Select(dropdown_element)
        select.select_by_value("az")

    def dropdown_for_descending_alphabet(self):
        dropdown_element = self.element_to_be_clickable(self.dropdown_btn)
        select = Select(dropdown_element)
        select.select_by_value("za")

    def dropdown_for_high_price(self):
        dropdown_element = self.element_to_be_clickable(self.dropdown_btn)
        select = Select(dropdown_element)
        select.select_by_value("hilo")

    def dropdown_for_low_price(self):
        dropdown_element = self.element_to_be_clickable(self.dropdown_btn)
        select = Select(dropdown_element)
        select.select_by_value("lohi")

    def get_product_names(self):
        elements = self.elements_to_be_visible(self.product_names)
        return [element.text for element in elements]

    def get_product_price(self):
        elements = self.elements_to_be_visible(self.product_prices)
        return [float(element.text.replace("$", "")) for element in elements]

    def is_sorted_by_name_asc(self):
        names = self.get_product_names()
        return names == sorted(names)

    def is_sorted_by_name_desc(self):
        names = self.get_product_names()
        return names == sorted(names, reverse=True)

    def is_sorted_by_price_high_low(self):
        prices = self.get_product_price()
        return prices == sorted(prices, reverse=True)

    def is_sorted_by_price_low_high(self):
        prices = self.get_product_price()
        return prices == sorted(prices)
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username_field = (By.XPATH, "//input[@id='user-name']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")
    error_message = (By.CSS_SELECTOR,"h3[data-test='error']")
    logo = (By.XPATH,"//div[@class='login_logo']")
    cart = (By.XPATH,"//a[@class='shopping_cart_link']")
    menu_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_link = (By.XPATH, "//a[@id='logout_sidebar_link']")
    inventory_container = (By.ID, "inventory_container")


    def get_username(self,username):
        self.element_to_be_visible(self.username_field).send_keys(username)


    def get_password(self,password):
         self.element_to_be_visible(self.password_field).send_keys(password)


    def click_login(self):
        self.element_to_be_clickable(self.login_button).click()

    #reusable method
    def login(self,username,password):
        self.get_username(username)
        self.get_password(password)
        self.click_login()

    def get_current_url(self):
        return self.driver.current_url

    def get_unauthenticated_page(self):
        element  = self.element_to_be_visible(self.logo)
        return element.text

    def is_cart_visible(self):
        cart = self.element_to_be_visible(self.cart)
        return cart.is_displayed()

    def get_error_messages(self):
        element =  self.element_to_be_visible(self.error_message)
        return element.text

    def click_menu_button(self):
        element = self.element_to_be_clickable(self.menu_button)
        element.click()

        self.element_to_be_visible(self.logout_link)

    def click_logout(self):
        element = self.element_to_be_visible(self.logout_link)
        element.click()

    def logout(self):
        self.click_menu_button()
        self.click_logout()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def element_to_be_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def elements_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from pages.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    def check_if_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10)\
                .until(EC.presence_of_element_located(ProductPageLocators.ADD_TO_CART_BUTTON))
            # using *ProductPageLocators.ADD_TO_CART_BUTTON generated an error because
            # presence_of_element_located() need tuple, not pair (By... , '')
            return True
        except TimeoutException:
            # Page didn't load propretly.
            return False

    def click_add_to_cart_button(self):
        pass

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

    def get_product_data(self):
        image = self.driver.find_element(*ProductPageLocators.PRODUCT_IMAGE)
        name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        description = self.driver.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text
        description = description.replace('Product description\n','')  # remove header
        price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price = price.replace(' *includes tax', '')
        product_data = {'image': image,
                        'name': name,
                        'description': description,
                        'price': price
        }
        return product_data


    def click_add_to_cart_button(self):
        pass

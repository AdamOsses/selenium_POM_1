from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page_locators import HomePageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class HomePage(BasePage):
    def check_if_contact_modal_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.CONTACT_MODAL)
        except NoSuchElementException:
            return False
        else:
            return True

    def check_if_about_us_modal_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.ABOUT_US_MODAL)
        except NoSuchElementException:
            return False
        else:
            return True

    def check_if_log_in_modal_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.LOG_IN_MODAL)
        except NoSuchElementException:
            return False
        else:
            return True

    def check_if_sign_up_modal_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.SIGN_UP_MODAL)
        except NoSuchElementException:
            return False
        else:
            return True

    def get_all_products_on_page(self):
        # this helps PyCharm to autocomplete
        # assert isinstance(self.driver, webdriver.Chrome())
        products = self.driver.find_elements(*HomePageLocators.PRODUCTS)
        return products

    def get_products_count_on_page(self):
        products_count = self.get_all_products_on_page()
        return len(products_count)

    def get_product_data_by_number(self, nr):
        # assert isinstance(self.driver, webdriver.Chrome())
        product_name = self.driver.find_element(*HomePageLocators.PRODUCT_NAME[nr]).text
        product_price = self.driver.find_element(*HomePageLocators.PRODUCT_PRICE[nr]).text
        product_description = self.driver.find_element(*HomePageLocators.PRODUCT_DESCRIPTION[nr]).text
        product_by_number = [product_name, product_price, product_description]
        return product_by_number

    def next_button_click(self):
        self.driver.find_element(*HomePageLocators.NEXT_BUTTON).click()

    def prev_button_click(self):
        self.driver.find_element(*HomePageLocators.PREVIOUS_BUTTON).click()


from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page_locators import HomePageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
# this helps PyCharm to autocomplete
# assert isinstance(self.driver, webdriver.Chrome())


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

    def check_if_log_in_button_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.LOG_IN_BUTTON)
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

    def check_if_log_out_button_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.LOG_OUT)
        except NoSuchElementException:
            return False
        else:
            return True

    def check_if_welkome_user_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.WELCOME_USER)
        except NoSuchElementException:
            return False
        else:
            return True

    def fill_username_field(self, name):
        #assert isinstance(self.driver, webdriver.Chrome())
        username_field = self.driver.find_element(*HomePageLocators.USERNAME_FIELD)
        username_field.click()
        username_field.clear()
        username_field.send_keys(name)

    def fill_password_field(self, password):
        password_field = self.driver.find_element(*HomePageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

    def log_in_modal_button_click(self):
        self.driver.find_element(*HomePageLocators.LOG_IN_BUTTON).click()

    # -------
    def get_all_products_on_page(self):
        products = self.driver.find_elements(*HomePageLocators.PRODUCTS)
        return products

    def get_products_count_on_page(self):
        products_count = self.get_all_products_on_page()
        return len(products_count)

    def get_product_data_by_number(self, nr):
        product_name = self.driver.find_element(*HomePageLocators.PRODUCT_NAME[nr]).text
        product_price = self.driver.find_element(*HomePageLocators.PRODUCT_PRICE[nr]).text
        product_description = self.driver.find_element(*HomePageLocators.PRODUCT_DESCRIPTION[nr]).text
        product_by_number = [product_name, product_price, product_description]
        return product_by_number

    def next_button_click(self):
        self.driver.find_element(*HomePageLocators.NEXT_BUTTON).click()

    def prev_button_click(self):
        self.driver.find_element(*HomePageLocators.PREVIOUS_BUTTON).click()


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

    def log_in_user(self, name, password):
        # assert isinstance(self.driver, webdriver.Chrome())
        self.driver.find_element(*HomePageLocators.LOG_IN).click()
        self.fill_username_field(name)
        self.fill_password_field(password)
        self.log_in_modal_button_click()

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

    def check_if_welcome_user_visible(self):
        try:
            self.driver.find_element(*HomePageLocators.WELCOME_USER)
        except NoSuchElementException:
            return False
        else:
            return True

    def return_name_of_logged_user(self):
        welcome_string = self.driver.find_element(*HomePageLocators.WELCOME_USER)
        user_name = welcome_string.text[8:]  # [8:] - slice off "Welcome "
        print(f'--{user_name}--')
        return user_name

    def fill_username_field(self, name):
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
        self.driver.find_element(*HomePageLocators.LOG_IN_MODAL_BUTTON).click()

    # ------- products --------------
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

    def get_all_products_data_on_page(self):
        all_product_data = []
        for i in range(0, self.get_products_count_on_page()):
            all_product_data.append(self.get_product_data_by_number(i))
        return all_product_data

    def next_button_click(self):
        self.driver.find_element(*HomePageLocators.NEXT_BUTTON).click()

    def prev_button_click(self):
        self.driver.find_element(*HomePageLocators.PREVIOUS_BUTTON).click()


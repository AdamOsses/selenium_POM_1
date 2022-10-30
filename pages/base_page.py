from selenium import webdriver
from pages.site_locators import SiteLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_url(self, name):
        return SiteLocators.PAGE_URL[name]

    # entire site buttons
    def home_button_click(self):
        self.driver.find_element(*SiteLocators.HOME).click()

    def contact_button_click(self):
        self.driver.find_element(*SiteLocators.CONTACT).click()

    def about_us_button_click(self):
        self.driver.find_element(*SiteLocators.ABOUT_US).click()

    def cart_button_click(self):
        self.driver.find_element(*SiteLocators.CART).click()

    def log_in_button_click(self):
        self.driver.find_element(*SiteLocators.LOG_IN).click()

    def sign_up_button_click(self):
        self.driver.find_element(*SiteLocators.SIGN_UP).click()

    def log_out_button_click(self):
        self.driver.find_element(*SiteLocators.LOG_OUT).click()







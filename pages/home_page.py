from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def get_products(self):
        # this helps PyCharm to autocomplete
        # assert isinstance(self.driver, webdriver.Chrome())
        products = self.driver.find_elements(*HomePageLocators.PRODUCTS)
        return products

    def next_button_click(self):
        self.driver.find_element(*HomePageLocators.NEXT_BUTTON).click()

    def prev_button_click(self):
        self.driver.find_element(*HomePageLocators.PREVIOUS_BUTTON).click()

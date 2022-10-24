from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def get_products(self):
        products = self.driver.find_elements(*HomePageLocators.PRODUCTS)
        # code completion not working here (PyCharm) ???
        return products










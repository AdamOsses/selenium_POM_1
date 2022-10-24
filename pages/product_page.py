from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    def click_product_store_icon(self):
        self.driver.find_element(*ProductPageLocators.PRODUCTS_STORE).click()

    def click_home_button(self):
        self.driver.find_element(*ProductPageLocators.HOME).click()

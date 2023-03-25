from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    # ====== Click on Product Store or Home should send us back to home page. ======
    def click_product_store_icon(self):
        self.driver.find_element(*ProductPageLocators.PRODUCTS_STORE).click()

    def click_home_button(self):
        self.driver.find_element(*ProductPageLocators.HOME).click()

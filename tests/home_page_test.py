import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from pages.product_page import ProductPage
from time import sleep


class HomePageTest(BaseTest):
    @unittest.skip("Skipping home page respond")
    def test_home_page_respond(self):
        print(f"Page {self.driver.current_url} working...")
        self.assertTrue(self.driver.current_url, "https://www.demoblaze.com/")

    def test_next_prev_button(self):
        pass

    def test_locators(self):
        # temp method for locator testing
        first_product = self.home_page.get_product_by_number(1)
        print(first_product)
        products = self.home_page.get_all_products_on_page()
        products[1].click()
        sleep(2)
        self.product_page = ProductPage(self.driver)
        self.product_page.click_product_store_icon()
        sleep(2)




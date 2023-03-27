import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from tests.base_test import HomePage
from pages.product_page import ProductPage
from time import sleep


class ProductPageTest(BaseTest):
    def create_pages(self):
        # Pages used by tests
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)

    # ======= Product Store and Home modal tests ========
    def test_product_store_click(self):
        product = self.home_page.get_product_data_by_number(0)
        product['product_href'].click()
        is_page = self.product_page.check_if_page_loaded()
        self.assertTrue(is_page, 'Page not loaded.')

        #  print(product['product_image'])
        #  product['product_image'].click()
        sleep(2)

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from pages.product_page import ProductPage
from time import sleep


class ProductPageTest(BaseTest):
    # ======= Product Store and Home modal tests ========

    def test_product_store_click(self):
        self.product_page = ProductPage(self.driver)
        product = self.home_page.get_product_data_by_number(0)
        print(f'Produkt: {product}')
        print((product['product_href']))
        product['product_href'].click()
        #print(product['product_image'])
        #product['product_image'].click()
        sleep(5)

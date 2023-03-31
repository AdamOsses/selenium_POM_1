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

    def test_name_price_desc_are_equal(self):
        # check if name, price, desc. are equal on main page and product page
        selected_product = self.home_page.get_product_data_by_number(0)
        selected_product['product_href'].click()
        data_on_product_page = self.product_page.get_product_data()
        name_equal_t_f = selected_product['product_name'] == data_on_product_page['name']
        price_equal_t_f = selected_product['product_price'] == data_on_product_page['price']
        description_equal_t_f = selected_product['product_description'] == data_on_product_page['description']
        # print(name, price, description, sep = '\n----------\n')
        all_t_f = name_equal_t_f and price_equal_t_f and description_equal_t_f
        # if one or more elements are not equal test will fail
        self.assertTrue(all_t_f, f'Same name = {name_equal_t_f}, '
                                 f'same price = {price_equal_t_f}, '
                                 f'same descr. = {description_equal_t_f}')





import unittest
import random
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

    def get_random_product(self):
        number_of_products = self.home_page.get_products_count_on_page()
        no = random.randint(0, number_of_products-1)
        product = self.home_page.get_product_data_by_number(no)
        # print(number_of_products, no, product, sep= '---->')
        return product

    def test_name_price_desc_are_equal(self):
        # check if name, price, desc. are equal on main page and product page
        selected_product = self.get_random_product()
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

    def test_add_to_cart_message(self):
        selected_product = self.get_random_product()
        selected_product['product_href'].click()
        sleep(1)
        self.product_page.click_add_to_cart_button()
        sleep(2)
        alert_box_text = self.driver.switch_to.alert.text
        print("Alert box msg.: " + alert_box_text)
        self.assertEqual(alert_box_text, 'Product added', 'Wrong alert box message.')






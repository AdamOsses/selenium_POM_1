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

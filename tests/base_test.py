import unittest
from selenium import webdriver
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    def create_pages(self):
        # Pages used by tests. Thanks to this method I don't have to overwrite
        # entire setUp method in product_page_tests.py
        self.home_page = HomePage(self.driver)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.driver.implicitly_wait(10)
        self.create_pages()
        #self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

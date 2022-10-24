import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from time import sleep


class HomePageTest(BaseTest):
    @unittest.skip("Skipping home page respond")
    def test_home_page_respond(self):
        print(f"Page {self.driver.current_url} working...")
        self.assertTrue(self.driver.current_url, "https://www.demoblaze.com/")

    def test_locators(self):
        # temp method for locator testing
        products = self.home_page.get_products()
        products[1].click()
        sleep(4)



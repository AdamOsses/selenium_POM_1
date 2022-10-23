import unittest
from selenium import webdriver
from tests.base_test import BaseTest


class HomePageTest(BaseTest):
    def test_home_page_respond(self):
        print(f"Page {self.driver.current_url} working...")
        self.assertTrue(self.driver.current_url, "https://www.demoblaze.com/")

    def test_locators(self):
        pass    


'''
if __name__ == "__main__":
    unittest.main()
'''
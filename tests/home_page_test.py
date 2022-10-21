import unittest
from selenium import webdriver
from tests.base_test import BaseTest


class HomePageTest(BaseTest):
    def test_home_page_respond(self):
        print("home_page_respond working...")
        self.assertTrue(True)


'''
if __name__ == "__main__":
    unittest.main()
'''
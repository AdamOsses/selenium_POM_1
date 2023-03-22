import unittest
from selenium import webdriver
from tests.base_test import BaseTest
from pages.product_page import ProductPage
from time import sleep


class HomePageTest(BaseTest):
    # @unittest.skip("test_home_page_respond")
    def test_home_page_respond(self):
        # print(f"Home page: {self.driver.current_url} working...")
        self.assertTrue(self.driver.current_url, self.home_page.get_page_url("home_page"))

    def test_product_store_button_click(self):
        products = self.home_page.get_all_products_on_page()
        products[0].click()
        product_page = ProductPage(self.driver)
        product_page.product_store_button_click()
        self.assertEqual(self.driver.current_url, self.home_page.get_page_url("home_page"))

    def test_home_button_click(self):
        products = self.home_page.get_all_products_on_page()
        products[0].click()
        product_page = ProductPage(self.driver)
        product_page.home_button_click()
        self.assertEqual(self.driver.current_url, self.home_page.get_page_url("home_page"))

    def test_contact_button_click(self):
        self.home_page.contact_button_click()
        self.assertTrue(self.home_page.check_if_contact_modal_visible(), "Contact modal not visible.")

    def test_about_us_button_click(self):
        self.home_page.about_us_button_click()
        self.assertTrue(self.home_page.check_if_about_us_modal_visible(), "About us modal not visible.")

    def test_log_out_button_click(self):
        self.home_page.log_in_user('ahk', 'ahk')
        self.assertTrue(self.home_page.check_if_log_out_button_visible(), "Log out button not visible.")
        # print(self.home_page.return_name_of_logged_user())
        self.home_page.log_out_button_click()
        self.assertFalse(self.home_page.check_if_log_out_button_visible(), "Log out still visible.")

    def test_log_in_button_click(self):
        self.home_page.log_in_button_click()
        self.assertTrue(self.home_page.check_if_log_in_modal_visible(), "Log in modal not visible.")

    def test_display_username(self):
        self.home_page.log_in_user('ahk', 'ahk')
        displayed_username = self.home_page.return_name_of_logged_user()
        self.assertEqual(displayed_username, 'ahk', 'Incorrect username displayed.')

    def test_log_in_no_password(self):
        # skip psswrd field
        self.home_page.log_in_button_click()
        self.home_page.fill_username_field('ahk')
        self.home_page.log_in_modal_button_click()
        # Alert popup box
        alert_box = self.driver.switch_to.alert
        msg = alert_box.text
        # print("Alert box msg.: " + msg)
        self.assertEqual(msg, 'Please fill out Username and Password.')

    def test_log_in_no_username(self):
        self.home_page.log_in_button_click()
        self.home_page.fill_password_field('ahk')
        self.home_page.log_in_modal_button_click()
        alert_box = self.driver.switch_to.alert
        msg = alert_box.text
        self.assertEqual(msg, 'Please fill out Username and Password.')

    def test_log_in_no_username_and_password(self):
        # skip psswrd and username field
        self.home_page.log_in_button_click()
        self.home_page.log_in_modal_button_click()
        alert_box = self.driver.switch_to.alert
        msg = alert_box.text
        self.assertEqual(msg, 'Please fill out Username and Password.')

    def test_sign_up_button_click(self):
        self.home_page.sign_up_button_click()
        self.assertTrue(self.home_page.check_if_sign_up_modal_visible(), "Sign up modal not visible.")

    def test_next_prev_button(self):
        page_1_products = self.home_page.get_all_products_data_on_page()
        self.home_page.next_button_click()
        sleep(1)  # reload products
        page_2_products = self.home_page.get_all_products_data_on_page()
        self.assertIsNotNone(page_2_products, "0 product on page after Next button click.")
        self.assertNotEqual(page_1_products, page_2_products, 'Same product list after Next button click.')
        self.home_page.prev_button_click()
        sleep(1)  # reload products
        page_1_products_after_prev = self.home_page.get_all_products_data_on_page()
        self.assertEqual(page_1_products, page_1_products_after_prev,
                         'Incorrect product list after Previous button click.')

    @unittest.skip("test_locators")
    def test_locators(self):
        # temp method for locator testing
        print(self.driver.current_url)
        home_url_test = self.home_page.get_page_url("home_page")
        print(f"Dict url: {home_url_test}")
        product_url_test = self.home_page.get_page_url("product_page")
        print(f"Product url: {product_url_test}")
        cart_url_test = self.home_page.get_page_url("cart_page")
        print(f"Cart url: {cart_url_test}")

        first_product = self.home_page.get_product_data_by_number(1)
        print(f"Prod no.1: {first_product}")
        products = self.home_page.get_all_products_on_page()
        products[1].click()
        sleep(2)
        print(f"Product page: {self.driver.current_url}")
        self.product_page = ProductPage(self.driver)
        self.product_page.click_product_store_icon()
        sleep(2)
        self.driver.get(self.product_page.get_page_url("cart_page"))
        sleep(2)






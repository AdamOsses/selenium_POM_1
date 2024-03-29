from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from tests.read_csv import read_csv_data


@ddt
class LogInTest(BaseTest):
    @data(["wrong_user_001", "wrong_password_001"], ["wrong_user_002", "wrong_password_002"])
    @unpack
    def test_wrong_username_and_password(self, username, password):
        self.home_page.log_in_button_click()
        self.home_page.fill_username_field(username)
        self.home_page.fill_password_field(password)
        self.home_page.log_in_modal_button_click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            log_in_alert_1 = self.driver.switch_to.alert
            log_in_alert_2 = Alert(self.driver)
            # ^^ Alertbox handling - two methods ^^

            self.assertEqual(log_in_alert_1.text, "User does not exist.", "! Alert present but wrong message. !")
            self.assertEqual(log_in_alert_2.text, "User does not exist.", "! Alert present but wrong message. !")
        except TimeoutException:
            self.assertTrue(False, "! Alertbox should be present. !")

    @data(*read_csv_data('tests/data.csv')) # * unpack whole list to rows
    @unpack
    def test_wrong_username_and_password_from_csv(self, username, password):
        self.home_page.log_in_button_click()
        self.home_page.fill_username_field(username)
        self.home_page.fill_password_field(password)
        self.home_page.log_in_modal_button_click()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            log_in_alert_1 = self.driver.switch_to.alert
            messages = ['User does not exist.', 'Wrong password.']
            self.assertIn(log_in_alert_1.text, messages, "! Alert present but wrong message. !")
        except TimeoutException:
            self.assertTrue(False, "! Alertbox should be present. !")

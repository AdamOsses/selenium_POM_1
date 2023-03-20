import unittest
from tests.home_page_test import HomePageTest
from tests.log_in_ddt import LogInTest
#from tests import log_in_ddt

test_case_to_test = "test_log_out_button_click"

# tests to run
tests_list = [
     unittest.TestLoader().loadTestsFromTestCase(LogInTest),
     #unittest.TestLoader().loadTestsFromTestCase(HomePageTest),
     #unittest.TestLoader().loadTestsFromName(f'tests.home_page_test.HomePageTest.{test_case_to_test}')
]

test_suite = unittest.TestSuite(tests_list)
unittest.TextTestRunner(verbosity=2).run(test_suite)

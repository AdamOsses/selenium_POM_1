import unittest
from tests.home_page_test import HomePageTest

test_case_to_test = "test_log_out_button_click"

# tests to run
tests_list = [
    # unittest.TestLoader().loadTestsFromTestCase(HomePageTest),
    unittest.TestLoader().loadTestsFromName(f'tests.home_page_test.HomePageTest.{test_case_to_test}')
]

test_suite = unittest.TestSuite(tests_list)
unittest.TextTestRunner().run(test_suite)

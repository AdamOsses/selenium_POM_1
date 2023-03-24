import unittest
from tests.home_page_test import HomePageTest
from tests.log_in_ddt import LogInTest

test_case_to_test = "test_carousel_next_prev_buttons"

# tests to run
tests_list = [
     # unittest.TestLoader().loadTestsFromTestCase(LogInTest),
     # unittest.TestLoader().loadTestsFromTestCase(HomePageTest),
     unittest.TestLoader().loadTestsFromName(f'tests.home_page_test.HomePageTest.{test_case_to_test}')
]

test_suite = unittest.TestSuite(tests_list)
unittest.TextTestRunner(verbosity=2).run(test_suite)

import unittest
from tests.home_page_test import HomePageTest
from tests.product_page_test import ProductPageTest
from tests.log_in_ddt import LogInTest

test_case_to_test = "test_add_to_cart_message"

# tests to run
tests_list = [
     # unittest.TestLoader().loadTestsFromTestCase(HomePageTest),
     # unittest.TestLoader().loadTestsFromTestCase(LogInTest),
     # unittest.TestLoader().loadTestsFromTestCase(ProductPageTest),
     # unittest.TestLoader().loadTestsFromName(f'tests.home_page_test.HomePageTest.{test_case_to_test}'),
     unittest.TestLoader().loadTestsFromName(f'tests.product_page_test.ProductPageTest.{test_case_to_test}')
]

test_suite = unittest.TestSuite(tests_list)
unittest.TextTestRunner(verbosity=2).run(test_suite)

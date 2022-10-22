import unittest
from tests.home_page_test import HomePageTest


# tests to run
tests_list = [
    unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
]

test_suite = unittest.TestSuite(tests_list)
unittest.TextTestRunner().run(test_suite)
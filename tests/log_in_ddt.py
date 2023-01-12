import unittest
from ddt import ddt, data, unpack
from tests.base_test import BaseTest

@ddt
class LogInTest(BaseTest):
    @data(["wrong_user_001", "wrong_password_001"])
    @unpack
    def test_wrong_username_and_password(self, username, password):
        pass


import unittest

from app.validators import check_username


class TestUserLogin(unittest.TestCase):
    def test_username_is_empty(self):
        """Check that user input not empty string"""

        self.assertIsNone(check_username(''))

    def test_username_start_with_digit(self):
        """Check that input string not start with digit"""

        self.assertIsNone(check_username('4reveryoung'))

    def test_special_characters_in_password(self):
        """Check invalid characters in user input"""

        self.assertIsNone(check_username('!sdf@@%'))

    def test_username_len_smaller_than_7(self):
        """Check length of user input for login"""

        self.assertIsNone(check_username('one'))

    def test_username_are_valid(self):
        """Check that user input for login does not start with digit and greater or equal to 7"""

        self.assertEqual(check_username('mysecret'), 'mysecret')

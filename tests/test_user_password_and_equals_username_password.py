import unittest

from app.validators import check_password, check_username_and_password_not_equals


class TestUserPassword(unittest.TestCase):
    def test_empty_user_password(self):
        """Check user input an empty string for password"""

        self.assertIsNone(check_password(''))

    def test_password_smaller_than_7(self):
        """Check user input smaller than 7 characters"""

        self.assertIsNone(check_password('pass'))

    def test_password_contains_only_letters(self):
        """Check user input contains only letters"""

        self.assertIsNone(check_password('password'))

    def test_password_contains_only_numbers(self):
        """Check user input contains only numbers"""

        self.assertIsNone(check_password('1234567'))

    def test_special_characters_in_password(self):
        """Check invalid characters in user input"""

        self.assertIsNone(check_password('!sdf@@%'))

    def test_valid_password(self):
        """Check user input contains letters and numbers"""

        self.assertEqual(check_password('123pass'), '123pass')

    def test_check_username_and_password_equals(self):
        """Check username and password the same"""

        self.assertFalse(check_username_and_password_not_equals(username='mamba', password='mamba'))

    def test_check_username_and_password_not_the_same(self):
        """Check username and password is different"""

        self.assertTrue(check_username_and_password_not_equals(username='mamba', password='limbo'))

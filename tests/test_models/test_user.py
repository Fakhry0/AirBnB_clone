#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def test_email_attribute(self):
        """Test that email attribute is an empty string"""
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """Test that password attribute is an empty string"""
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """Test that first_name attribute is an empty string"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """Test that last_name attribute is an empty string"""
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()

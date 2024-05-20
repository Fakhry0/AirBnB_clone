#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_new_instance_is_valid(self):
        """Test creating a new instance of User."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_attributes_are_correct_types(self):
        """Test the types of User attributes."""
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_two_users_have_different_ids(self):
        """Test that two User instances have unique IDs."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_str_representation(self):
        """Test the string representation of a User instance."""
        user = User()
        user.id = "123456"
        user_str = str(user)
        expected_str = f"[User] (123456) {user.__dict__}"
        self.assertEqual(user_str, expected_str)

    def test_instantiation_with_kwargs(self):
        """Test creating a User instance with keyword arguments."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso,
                    email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


class TestUser_save(unittest.TestCase):
    """Unittests for testing the save method of the User class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_updates_updated_at(self):
        """Test that save updates the updated_at attribute."""
        user = User()
        sleep(0.05)
        initial_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(initial_updated_at, user.updated_at)

    def test_save_updates_file(self):
        """Test that save updates the JSON file."""
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(user_id, content)


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the User class."""

    def test_to_dict_returns_a_dictionary(self):
        """Test that to_dict returns a dictionary."""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        user = User()
        user_dict = user.to_dict()
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)

    def test_to_dict_values_are_correct_types(self):
        """Test that to_dict values are of the correct types."""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict["id"], str)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)
        self.assertIsInstance(user_dict["__class__"], str)
        self.assertIsInstance(user_dict["email"], str)
        self.assertIsInstance(user_dict["password"], str)
        self.assertIsInstance(user_dict["first_name"], str)
        self.assertIsInstance(user_dict["last_name"], str)


if __name__ == "__main__":
    unittest.main()

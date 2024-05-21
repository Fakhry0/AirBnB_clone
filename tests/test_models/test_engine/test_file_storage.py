#!/usr/bin/python3

"""
Unittest for FileStorage
"""

import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorageWithUser(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        self.user = User(email="test@example.com",
                         password="password", first_name="John", last_name="Doe")
        self.user.save()

    def tearDown(self):
        """Remove the JSON file after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_user_added_to_objects(self):
        """Test that user is added to __objects"""
        key = f"{self.user.__class__.__name__}.{self.user.id}"
        self.assertIn(key, self.storage.all())

    def test_user_serialized_to_json(self):
        """Test that user is serialized to JSON file"""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            data = json.load(f)
            self.assertIn(
                f"{self.user.__class__.__name__}.{self.user.id}", data)

    def test_user_deserialized_from_json(self):
        """Test that user is deserialized from JSON file"""
        self.storage.save()
        self.storage.reload()
        key = f"{self.user.__class__.__name__}.{self.user.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()

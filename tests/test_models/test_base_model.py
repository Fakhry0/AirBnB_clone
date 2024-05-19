#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
from models import storage
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test methods."""
        self.model = BaseModel()

    def test_id(self):
        """Test if id is a string and has the right format."""
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(len(self.model.id) > 0)

    def test_created_at(self):
        """Test if created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method."""
        expected_str = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    # Create a new instance of BaseModel
    new_instance = BaseModel()
    new_instance.name = "Test"
    new_instance.number = 42
    new_instance.save()

    # Check the storage content
    all_objs = storage.all()
    print(all_objs)

    # Reload the storage and check again
    storage.reload()
    all_objs = storage.all()
    print(all_objs)


if __name__ == "__main__":
    unittest.main()

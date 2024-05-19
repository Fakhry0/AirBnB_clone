#!/usr/bin/python3
"""
Unittest for BaseModel and FileStorage
"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test methods."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Tear down test methods."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test if BaseModel instance is created correctly."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_save_method(self):
        """Test if the save method updates 'updated_at' and saves to storage."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)
        key = "BaseModel." + obj.id
        self.assertIn(key, storage.all())

    def test_to_dict_method(self):
        """Test if to_dict method creates a dictionary with proper attrs."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_reload_method(self):
        """Test if the reload method correctly restores objects from file."""
        obj = BaseModel()
        obj_id = obj.id
        obj.save()
        storage.save()
        storage.reload()
        key = "BaseModel." + obj_id
        self.assertIn(key, storage.all())

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)
        self.assertNotIn("__class__", new_obj.__dict__)


if __name__ == '__main__':
    unittest.main()

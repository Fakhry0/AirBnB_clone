#!/usr/bin/python3
"""Test BaseModel"""

import unittest
from models.base_model import BaseModel
from models import storage
import os
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Remove the JSON file after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_init(self):
        """Test that a new instance is correctly initialized"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertEqual(self.model.created_at, self.model.updated_at)
        self.assertAlmostEqual(self.model.created_at,
                               self.model.updated_at, delta=timedelta(seconds=1))

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_save(self):
        """Test that save updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        time.sleep(1)  # Ensure time has passed
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_save_creates_file(self):
        """Test that save creates a file"""
        self.model.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_new_instance_added_to_storage(self):
        """Test that a new instance is added to storage"""
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, storage.all())

    def test_reload(self):
        """Test that reload properly loads objects from file.json"""
        self.model.save()
        storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()

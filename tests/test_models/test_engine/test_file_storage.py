#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.model = BaseModel()

    def tearDown(self):
        """Remove storage file at end of tests."""
        try:
            os.remove("test_file.json")
        except IOError:
            pass

    def test_file_path(self):
        """Test __file_path attribute."""
        self.assertEqual(self.storage._FileStorage__file_path,
                         "test_file.json")

    def test_all(self):
        """Test all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method."""
        self.storage.new(self.model)
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def test_save(self):
        """Test save method."""
        self.storage.new(self.model)
        self.storage.save()
        with open("test_file.json", "r") as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{self.model.id}", data)

    def test_reload(self):
        """Test reload method."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())


if __name__ == "__main__":
    unittest.main()

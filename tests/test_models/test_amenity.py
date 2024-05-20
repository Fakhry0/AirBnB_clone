#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_new_instance_is_valid(self):
        """Test creating a new instance of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

    def test_attributes_are_correct_types(self):
        """Test the types of Amenity attributes."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.name, str)

    def test_two_amenities_have_different_ids(self):
        """Test that two Amenity instances have unique IDs."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_str_representation(self):
        """Test the string representation of an Amenity instance."""
        amenity = Amenity()
        amenity.id = "123456"
        amenity_str = str(amenity)
        expected_str = f"[Amenity] (123456) {amenity.__dict__}"
        self.assertEqual(amenity_str, expected_str)

    def test_instantiation_with_kwargs(self):
        """Test creating an Amenity instance with keyword arguments."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso,
                          name="Swimming Pool")
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)
        self.assertEqual(amenity.name, "Swimming Pool")


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing the save method of the Amenity class."""

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
        amenity = Amenity()
        sleep(0.05)
        initial_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(initial_updated_at, amenity.updated_at)

    def test_save_updates_file(self):
        """Test that save updates the JSON file."""
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(amenity_id, content)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the Amenity class."""

    def test_to_dict_returns_a_dictionary(self):
        """Test that to_dict returns a dictionary."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)
        self.assertIn("name", amenity_dict)

    def test_to_dict_values_are_correct_types(self):
        """Test that to_dict values are of the correct types."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict["id"], str)
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)
        self.assertIsInstance(amenity_dict["__class__"], str)
        self.assertIsInstance(amenity_dict["name"], str)


if __name__ == "__main__":
    unittest.main()

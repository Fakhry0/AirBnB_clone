#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_new_instance_is_valid(self):
        """Test creating a new instance of City."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_attributes_are_correct_types(self):
        """Test the types of City attributes."""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_two_cities_have_different_ids(self):
        """Test that two City instances have unique IDs."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_str_representation(self):
        """Test the string representation of a City instance."""
        city = City()
        city.id = "123456"
        city_str = str(city)
        expected_str = f"[City] (123456) {city.__dict__}"
        self.assertEqual(city_str, expected_str)

    def test_instantiation_with_kwargs(self):
        """Test creating a City instance with keyword arguments."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso,
                    state_id="CA", name="San Francisco")
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")


class TestCity_save(unittest.TestCase):
    """Unittests for testing the save method of the City class."""

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
        city = City()
        sleep(0.05)
        initial_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(initial_updated_at, city.updated_at)

    def test_save_updates_file(self):
        """Test that save updates the JSON file."""
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(city_id, content)


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the City class."""

    def test_to_dict_returns_a_dictionary(self):
        """Test that to_dict returns a dictionary."""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        city = City()
        city_dict = city.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)

    def test_to_dict_values_are_correct_types(self):
        """Test that to_dict values are of the correct types."""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict["id"], str)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertIsInstance(city_dict["__class__"], str)
        self.assertIsInstance(city_dict["state_id"], str)
        self.assertIsInstance(city_dict["name"], str)


if __name__ == "__main__":
    unittest.main()

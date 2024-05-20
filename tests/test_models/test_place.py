#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_new_instance_is_valid(self):
        """Test creating a new instance of Place."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_attributes_are_correct_types(self):
        """Test the types of Place attributes."""
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_two_places_have_different_ids(self):
        """Test that two Place instances have unique IDs."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_str_representation(self):
        """Test the string representation of a Place instance."""
        place = Place()
        place.id = "123456"
        place_str = str(place)
        expected_str = f"[Place] (123456) {place.__dict__}"
        self.assertEqual(place_str, expected_str)

    def test_instantiation_with_kwargs(self):
        """Test creating a Place instance with keyword arguments."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        place = Place(id="345", created_at=dt_iso, updated_at=dt_iso,
                      city_id="SF", user_id="123", name="My Place",
                      description="A great place", number_rooms=2,
                      number_bathrooms=1, max_guest=4, price_by_night=100,
                      latitude=37.7749, longitude=-122.4194,
                      amenity_ids=["wifi", "parking"])
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, dt)
        self.assertEqual(place.updated_at, dt)
        self.assertEqual(place.city_id, "SF")
        self.assertEqual(place.user_id, "123")
        self.assertEqual(place.name, "My Place")
        self.assertEqual(place.description, "A great place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["wifi", "parking"])


class TestPlace_save(unittest.TestCase):
    """Unittests for testing the save method of the Place class."""

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
        place = Place()
        sleep(0.05)
        initial_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(initial_updated_at, place.updated_at)

    def test_save_updates_file(self):
        """Test that save updates the JSON file."""
        place = Place()
        place.save()
        place_id = "Place." + place.id
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(place_id, content)


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the Place class."""

    def test_to_dict_returns_a_dictionary(self):
        """Test that to_dict returns a dictionary."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertIn("description", place_dict)
        self.assertIn("number_rooms", place_dict)
        self.assertIn("number_bathrooms", place_dict)
        self.assertIn("max_guest", place_dict)
        self.assertIn("price_by_night", place_dict)
        self.assertIn("latitude", place_dict)
        self.assertIn("longitude", place_dict)
        self.assertIn("amenity_ids", place_dict)

    def test_to_dict_values_are_correct_types(self):
        """Test that to_dict values are of the correct types."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict["id"], str)
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)
        self.assertIsInstance(place_dict["__class__"], str)
        self.assertIsInstance(place_dict["city_id"], str)
        self.assertIsInstance(place_dict["user_id"], str)
        self.assertIsInstance(place_dict["name"], str)
        self.assertIsInstance(place_dict["description"], str)
        self.assertIsInstance(place_dict["number_rooms"], int)
        self.assertIsInstance(place_dict["number_bathrooms"], int)
        self.assertIsInstance(place_dict["max_guest"], int)
        self.assertIsInstance(place_dict["price_by_night"], int)
        self.assertIsInstance(place_dict["latitude"], float)
        self.assertIsInstance(place_dict["longitude"], float)
        self.assertIsInstance(place_dict["amenity_ids"], list)


if __name__ == "__main__":
    unittest.main()

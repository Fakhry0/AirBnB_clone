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

    def test_state(self):
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_city(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_amenity(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_place(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        # Add more assertions for other attributes
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_review(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))


if __name__ == '__main__':
    unittest.main()

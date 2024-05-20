#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_new_instance_is_valid(self):
        """Test creating a new instance of Review."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_attributes_are_correct_types(self):
        """Test the types of Review attributes."""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_two_reviews_have_different_ids(self):
        """Test that two Review instances have unique IDs."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_str_representation(self):
        """Test the string representation of a Review instance."""
        review = Review()
        review.id = "123456"
        review_str = str(review)
        expected_str = f"[Review] (123456) {review.__dict__}"
        self.assertEqual(review_str, expected_str)

    def test_instantiation_with_kwargs(self):
        """Test creating a Review instance with keyword arguments."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        review = Review(id="345", created_at=dt_iso, updated_at=dt_iso,
                        place_id="789", user_id="123", text="Great place!")
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)
        self.assertEqual(review.place_id, "789")
        self.assertEqual(review.user_id, "123")
        self.assertEqual(review.text, "Great place!")


class TestReview_save(unittest.TestCase):
    """Unittests for testing the save method of the Review class."""

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
        review = Review()
        sleep(0.05)
        initial_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(initial_updated_at, review.updated_at)

    def test_save_updates_file(self):
        """Test that save updates the JSON file."""
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(review_id, content)


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the Review class."""

    def test_to_dict_returns_a_dictionary(self):
        """Test that to_dict returns a dictionary."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)

    def test_to_dict_values_are_correct_types(self):
        """Test that to_dict values are of the correct types."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict["id"], str)
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)
        self.assertIsInstance(review_dict["__class__"], str)
        self.assertIsInstance(review_dict["place_id"], str)
        self.assertIsInstance(review_dict["user_id"], str)
        self.assertIsInstance(review_dict["text"], str)


if __name__ == "__main__":
    unittest.main()

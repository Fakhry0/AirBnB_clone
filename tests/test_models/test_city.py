#!/usr/bin/python3
"""
Unittest for City class.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()

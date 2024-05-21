#!/usr/bin/python3
"""
Unittest for State class.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()

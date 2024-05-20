#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_new_instance_is_valid(self):
        """Test creating a new instance of State."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

    def test_attributes_are_correct_types(self):
        """Test the types of State attributes."""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)

    def test_two_states_have_different_ids(self):
        """Test that two State instances have unique IDs."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_str_representation(self):
        """Test the string representation of a State instance."""
        state = State()
        state.id = "123456"
        state_str = str(state)
        expected_str = f"[State] (123456) {state.__dict__}"
        self.assertEqual(state_str, expected_str)

    def test_instantiation_with_kwargs(self):
        """Test creating a State instance with keyword arguments."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso,
                      name="California")
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)
        self.assertEqual(state.name, "California")


class TestState_save(unittest.TestCase):
    """Unittests for testing the save method of the State class."""

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
        state = State()
        sleep(0.05)
        initial_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(initial_updated_at, state.updated_at)

    def test_save_updates_file(self):
        """Test that save updates the JSON file."""
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(state_id, content)


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the State class."""

    def test_to_dict_returns_a_dictionary(self):
        """Test that to_dict returns a dictionary."""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        state = State()
        state_dict = state.to_dict()
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)
        self.assertIn("name", state_dict)

    def test_to_dict_values_are_correct_types(self):
        """Test that to_dict values are of the correct types."""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict["id"], str)
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)
        self.assertIsInstance(state_dict["__class__"], str)
        self.assertIsInstance(state_dict["name"], str)


if __name__ == "__main__":
    unittest.main()

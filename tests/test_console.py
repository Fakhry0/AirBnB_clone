#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
import os


class TestHBNBCommand(unittest.TestCase):
    """Tests for the HBNBCommand class"""

    def setUp(self):
        """Set up test environment"""
        storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistentClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show(self):
        """Test show command"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {obj.id}")
            self.assertIn(obj.id, f.getvalue().strip())

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NonExistentClass some_id")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel some_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy(self):
        """Test destroy command"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {obj.id}")
            self.assertNotIn(obj.id, storage.all())

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NonExistentClass some_id")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel some_id")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        """Test all command"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIn(obj.id, f.getvalue().strip())

    def test_all_class(self):
        """Test all command with class name"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn(obj.id, f.getvalue().strip())

    def test_all_invalid_class(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all NonExistentClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update(self):
        """Test update command"""
        obj = BaseModel()  # Make sure to use BaseModel
        storage.new(obj)
        storage.save()
        print(f"Object ID: {obj.id}")  # Debug print
        print(f"Storage contents: {storage.all()}")  # Debug print

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj.id} name 'Updated'")
            print(f"Storage after update: {storage.all()}")  # Debug print
            self.assertEqual(
                storage.all()[f"BaseModel.{obj.id}"].name, "Updated")

    def test_update_missing_class(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NonExistentClass some_id name 'Updated'")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel some_id name 'Updated'")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute(self):
        """Test update command with missing attribute name"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj.id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with missing attribute value"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {obj.id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_with_dictionary(self):
        """Test update command with dictionary"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f'update BaseModel {obj.id} {{"name": "Updated", "number": 89}}')
            self.assertEqual(
                storage.all()[f"BaseModel.{obj.id}"].name, "Updated")
            self.assertEqual(storage.all()[f"BaseModel.{obj.id}"].number, 89)


if __name__ == "__main__":
    unittest.main()

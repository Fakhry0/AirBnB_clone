#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""

import json
from os.path import exists


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                from models.base_model import BaseModel
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)

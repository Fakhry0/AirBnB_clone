#!/usr/bin/python3
"""
FileStorage module for serializing and deserializing JSON files.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    # Assumes class is imported globally
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

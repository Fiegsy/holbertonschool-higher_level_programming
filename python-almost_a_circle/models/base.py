#!/usr/bin/python3
"""The first class"""
import json
import os


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance"""
        self.id = id if id is not None else Base.__nb_objects + 1
        Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        list_objs = list_objs or []
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dict_list)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON representation json_string."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding="utf-8") as file:
            json_file = file.read()
            new_dict = cls.from_json_string(json_file)
            instances = [cls.create(**data) for data in new_dict]
        return instances
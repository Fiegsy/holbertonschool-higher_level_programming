#!/usr/bin/python3
"""Module defining the Base class"""

import json
from os.path import exists


class Base:
    """Defines the attributes and methods of the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for the Base class.

        Args:
            id (int): Positive integer to set class instance's id to.
        """
        self.id = id if id is not None else Base.__nb_objects + 1
        Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of 'list_dictionaries'"""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file"""
        list_objs = list_objs or []
        my_list = [obj.to_dictionary() for obj in list_objs]
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            f.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON representation 'json_string'"""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""
        dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file containing JSON string
        representation of a class 'cls' object"""
        filename = f"{cls.__name__}.json"
        if not exists(filename):
            return []
        with open(filename, "r") as f:
            json_str = f.read()
            json_list = cls.from_json_string(json_str)
            return [cls.create(**dict) for dict in json_list]
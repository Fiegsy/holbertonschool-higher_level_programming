#!/usr/bin/python3
"""Module that defines the Student class"""


class Student:
    """Defines the Student class"""

    def __init__(self, first_name, last_name, age):
        """Constructor method for the Student class.

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation for JSON serialization of
        an object"""

        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json_data):
        """Replaces all attributes of the Student instance"""
        
        for attr, value in json_data.items():
            setattr(self, attr, value)
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

    def to_dict(self):
        """Returns a dictionary representation of the student"""

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
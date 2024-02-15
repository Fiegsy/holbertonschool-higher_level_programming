#!/usr/bin/python3
"""Module JSON"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_dict(self):
        """Returns a dictionary representation of the student"""
        return self.__dict__
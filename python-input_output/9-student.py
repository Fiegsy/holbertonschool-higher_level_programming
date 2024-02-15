#!/usr/bin/python3
"""module JSON to define class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize a new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
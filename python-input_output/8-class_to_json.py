#!/usr/bin/python3
"""Module with a function that returns the simple description for
JSON serialization of an object"""


def class_to_json(obj):
    """Returns the dictionnary description with simple data structure
    for the JSON serialization of 'obj'"""

    return obj.__dict__
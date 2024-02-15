#!/usr/bin/python3
"""Module with a function that returns a simple description for JSON serialization of an object"""


def obj_to_json(obj):
    """Returns a dictionary description with simple data structure for the JSON serialization of 'obj'"""

    return obj.__dict__
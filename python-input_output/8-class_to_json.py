#!/usr/bin/python3
"""Module with a function to convert an object to a dictionary for JSON serialization"""


def obj_to_json(obj):
    """Returns a dictionary representation of the object suitable for JSON serialization"""

    return obj.__dict__
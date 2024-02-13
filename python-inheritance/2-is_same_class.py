#!/usr/bin/python3
"""Function that checks if an object is an instance of a specified class"""


def is_instance_of(obj, a_class):
    """Function to determine if obj is an instance of a_class"""
    return True if isinstance(obj, a_class) else False
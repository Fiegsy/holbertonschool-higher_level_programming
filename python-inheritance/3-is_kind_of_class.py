#!/usr/bin/python3
"""Function to check if an object is an instance of a class or one of its derived classes"""


def is_instance_or_subclass(obj, a_class):
    """Check if an object is an instance of a specified class or one of its derived classes"""
    return isinstance(obj, a_class)
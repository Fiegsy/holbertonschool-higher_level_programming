#!/usr/bin/python3
"""Function that returns if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of the specified class or a subclass"""
    return isinstance(obj, a_class)
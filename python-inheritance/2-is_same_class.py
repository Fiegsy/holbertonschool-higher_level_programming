#!/usr/bin/python3
"""Module with a function to check if an object is an instance of a class"""


def is_instance_of(obj, a_class):
    """Checks if an object is exactly an instance of the specified class"""
    return type(obj) is a_class
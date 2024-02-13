#!/usr/bin/python3
"""Module defining the BaseGeometry class"""


class BaseGeometry:
    """Defines the BaseGeometry class"""

    def area(self):
        """Raises an exception if area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer greater than 0"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
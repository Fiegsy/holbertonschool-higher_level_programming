#!/usr/bin/python3
"""Module where the BaseGeometry class is defined"""


class BaseGeometry:
    """Defines the BaseGeometry class"""

    def area(self):
        """Computes the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if 'value' has the excepted type and within the excpected
        range.

        Args:
            name (string): The object attribute's name
            value (unknown): The object attribute's value

        Raises:
            TypeError: if 'value' is not an integer
            ValueError: if 'value' is less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
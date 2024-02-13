#!/usr/bin/python3
"""Module defining the BaseGeometry class"""


class BaseGeometry:
    """Defines the BaseGeometry class"""

    def area(self):
        """Raises an exception"""
        raise NotImplementedError("area() is not implemented")
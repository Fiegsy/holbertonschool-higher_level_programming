#!/usr/bin/python3
"""Module with the Square class"""

from typing import Union

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class"""

    def __init__(self, size: Union[int, float]):
        """Constructor method to instantiate a Square object

        Args:
            size (int or float): Defines the size of the square
        """

        super().__init__(size, size)

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] {}/{}".format(self.width, self.height)
    
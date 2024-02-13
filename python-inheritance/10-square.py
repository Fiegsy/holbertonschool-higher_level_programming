#!/usr/bin/python3
"""Geometry module"""

from typing import Union

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size: Union[int, float]):
        """Initializes a new square.

        Args:
            size (int or float): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self) -> Union[int, float]:
        """Calculates the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2
#!/usr/bin/python3
"""Module with the Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Rectangle class"""

    def __init__(self, size):
        """Constructor method to instanciate a Square object

        Args:
            size (int): Defines the size of the square
        """

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
    
#!/usr/bin/python3
"""Module with the Square class"""

from rectangle import Rectangle

class Square(Rectangle):
    """Defines the Square class"""

    def __init__(self, size):
        """Constructor method to instantiate a Square object

        Args:
            size (int): Defines the size of the square
        """

        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
"""Module with a Square class containing attributes"""


class Square:
    """Class to define a square of a given size"""
    def __init__(self, size=0, color='white', filled=True):
        """Initialize a square to a given size.

        Args:
            size (int, optional): Size of the square.
                Defaults to 0. Stored as a private attribute
            color (str, optional): Color of the square.
                Defaults to 'white'. Stored as a private attribute
            filled (bool, optional): Whether the square is filled.
                Defaults to True. Stored as a private attribute

        Raises:
            TypeError: If the size attribute is not an integer.
            ValueError: If the size attribute is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__color = color
        self.__filled = filled

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        The value must be an integer greater than or equal to 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def color(self):
        """Get the color of the square."""
        return self.__color

    @color.setter
    def color(self, value):
        """Set the color of the square."""
        self.__color = value

    @property
    def filled(self):
        """Check if the square is filled."""
        return self.__filled

    @filled.setter
    def filled(self, value):
        """Set whether the square is filled."""
        self.__filled = value
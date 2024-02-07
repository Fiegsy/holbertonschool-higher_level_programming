#!/usr/bin/python3
"""empty module"""


class Rectangle:
    """class to calculate size of area"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        if width < 0 or height < 0:
            raise ValueError("width and height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        """function to return area"""
        return self.__width * self.__height

    @property
    def width(self):
        """property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise ValueError("width must be an integer")

    @property
    def height(self):
        """property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if isinstance(value, int):
            self.__height = value
        else:
            raise ValueError("height must be an integer")
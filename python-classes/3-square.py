#!/usr/bin/python3
"""empty module"""


class Rectangle:
    """class to calculate area"""
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
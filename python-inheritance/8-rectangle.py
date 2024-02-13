#!/usr/bin/python3
"""Module defining the Rectangle class"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Defines the Rectangle class, which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with the given width and height"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
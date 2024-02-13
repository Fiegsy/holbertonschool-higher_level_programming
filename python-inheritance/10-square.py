#!/usr/bin/python3
"""Geometry module"""
from base_geometry import BaseGeometry
from rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square"""

    def __init__(self, size):
        """Initializes a new square"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
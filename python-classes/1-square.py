#!/usr/bin/python3
"""Module with a Square class containing attributes"""


class Square:
    """Class that keeps a square's size private"""
    def __init__(self, size):
        """Method to keep size as a private instance
        Args:
            size (int): Size of the square"""
        self.__size = size

#!/usr/bin/python3
"""Module defining a Rectangle class inheriting from Base"""

from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance."""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_non_negative_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_non_negative_integer(value, "height")
      

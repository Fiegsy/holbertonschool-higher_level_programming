#!/usr/bin/python3
"""Module defining the Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Defines the attributes and methods of the Rectangle class that
    inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for the Rectangle class.

        Args:
            width (int): Determines the width of the Rectangle instance
            height (int): Determines the height of the Rectangle instance
            x (int): Position of the object on the x axis
            y (int): Position of the object on the y axis
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the 'width' private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle instance

        Args:
            value (int): Positive integer

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the 'height' private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle instance

        Args:
            value (int): Positive integer

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the 'x' private instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x position of the Rectangle instance

        Args:
            value (int): Positive integer

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the 'y' private instance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y position of the Rectangle instance

        Args:
            value (int): Positive integer

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes and returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints out the Rectangle instance with '#'s"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Defines the string representation of a Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Allows a user to update a Rectangle instance's attributes after
        it was created.

        Args:
            id (int, optional): Integer to set the Rectangle instance's id to
            width (int, optional): New width of the instance
            height (int, optional): New height of the instance
            x (int, optional): New x position of the instance
            y (int, optional): New y position of the instance

            **kwargs (dict): key/value pairs of attributes
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

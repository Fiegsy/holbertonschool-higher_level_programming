#!/usr/bin/python3
"""empty module"""


class Rectangle:
    """a class create rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        Rectangle.number_of_instances += 1

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        str_rectangle = ''
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                if i == self.__height - 1:
                    str_rectangle += '#' * self.__width
                else:
                    str_rectangle += '#' * self.__width + '\n'
        return str_rectangle

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def get_number_of_instances(self):
        return Rectangle.number_of_instances
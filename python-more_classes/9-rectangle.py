#!/usr/bin/python3
"""Module with a rectangle class"""


class Rectangle:
    """Class that defines a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        Defaults to 0.
        print_symbol (any type): The default symbol for string representation.
        First initialized to '#'.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Class constructor method for instantiation of rectangle object.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle.

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the rectangle.

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of a rectangle.

        Returns: The perimeter of the rectangle, or 0 if height or width
        is zero
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Returns a string representation of a rectangle object with the
        character '#', or an empty string if width or height is zero"""

        rectangle = ""
        newline = ""
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                rectangle += newline + str(self.print_symbol) * self.__width
                newline = "\n"

        return rectangle

    def __repr__(self):
        """Return an 'official' printable string representation of a
        rectangle object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print out a message when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare the areas of two rectangles.

        Args:
            rect_1 (obj): Object of the Rectangle class
            rect_2 (obj): Object of the Rectangle class

        Returns:
            The object with the biggest area

        Raises:
            TypeError: If either of arguments is not a rectangle object
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a square object of the given size.

        Args:
            cls (class): conventional name used for the class itself in
                a class method.
                It is similar to the "self" parameter used in instance methods,
                but instead of referring to an instance of the class, it refers
                to the class itself.

            size (int, optional): The height and width of the rectangle
            to create.

        Returns:
            A new instance of the Rectangle class with both width and
            height equal to 'size'--> a square.
        """

        return cls(size, size)
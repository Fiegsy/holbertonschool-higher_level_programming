#!/usr/bin/python3
"""a module with my class"""


class Square:
    """A class that creates a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than 0 or position contains negative integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 \
           or not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If any coordinate in value is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

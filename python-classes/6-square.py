#!/usr/bin/python3
"""Module with a Square class that defines more attributes"""


class Square:
    """Class to define a square of a given size and position"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than zero or position contains non-positive integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of two integers")
        if not all(isinstance(coord, int) for coord in position):
            raise TypeError("position coordinates must be integers")
        if any(coord < 0 for coord in position):
            raise ValueError("position coordinates must be >= 0")
            
        self.__size = size
        self.__position = position

    def area(self):
        """Compute the area of the square.

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
            ValueError: If value is less than zero.
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
            TypeError: If value is not a tuple of two integers.
            ValueError: If any coordinate in value is less than zero.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of two integers")
        if not all(isinstance(coord, int) for coord in value):
            raise TypeError("position coordinates must be integers")
        if any(coord < 0 for coord in value):
            raise ValueError("position coordinates must be >= 0")
        self.__position = value

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

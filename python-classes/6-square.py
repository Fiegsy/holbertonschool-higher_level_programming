class Rectangle:
    """Class to define a rectangle of a given size and position"""
    def __init__(self, width=0, height=0, position=(0, 0)):
        """Initialize a rectangle to a given width and height.

        Args:
            width (int, optional): Width of the rectangle.
                Defaults to 0. Stored as a private attribute
            height (int, optional): Height of the rectangle.
                Defaults to 0. Stored as a private attribute
            position(tup, optional): Tuple representing the spatial
                position of the rectangle. Defaults to (0, 0).
                Stored as a private attribute.

        Raises:
            TypeError: If the width, height, or position attributes are not of the expected types.
            ValueError: If the width or height attributes are less than zero.
        """
        self.position = position
        if not isinstance(width, int) or not isinstance(height, int) or not isinstance(position, tuple):
            raise TypeError("width, height, and position must be integers and a tuple respectively")
        if width < 0 or height < 0 or len(position) != 2 or not all(isinstance(coord, int) for coord in position):
            raise ValueError("width and height must be >= 0, position must be a tuple of two integers")
        self.__width = width
        self.__height = height

    def area(self):
        """Compute the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        The value must be an integer greater than or equal to 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        The value must be an integer greater than or equal to 0.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def position(self):
        """Get the position of the rectangle."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the rectangle.

        The value must be a tuple of two integers representing the x and y coordinates.

        Raises:
            TypeError: If the value is not a tuple of two integers.
            ValueError: If the coordinates are less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(coord, int) for coord in value):
            raise TypeError("position must be a tuple of two integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("coordinates must be >= 0")
        self.__position = value

    def my_print(self):
        """Print out a rectangle with the character '#'."""
        if self.__height == 0 or self.__width == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__height):
            print(" " * self.__position[0] + "#" * self.__width)
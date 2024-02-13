#!/usr/bin/python3
"""Module où la classe Square est définie"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe représentant un carré"""

    def __init__(self, size):
        """Initialise un nouveau carré"""

        super().__init__(size, size)  # Appel au constructeur de la classe parente (Rectangle)
        self.__size = size

    def area(self):
        """Calcule et retourne l'aire du carré"""

        return self.__size ** 2
    
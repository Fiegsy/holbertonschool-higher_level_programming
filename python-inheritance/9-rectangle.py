#!/usr/bin/python3
"""Module où la classe Rectangle est définie"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Définit la classe Rectangle qui hérite de BaseGeometry"""

    def __init__(self, width, height):
        """Initialise les attributs de l'objet lors de l'instanciation

        Args:
            width (int): Définit la largeur de l'objet
            height (int): Définit la hauteur de l'objet
        """

        super().__init__()  # Appel au constructeur de la classe parente (BaseGeometry)
        self.width = width
        self.height = height

    def area(self):
        """Calcule et retourne l'aire du rectangle"""

        return self.width * self.height

    def __str__(self):
        """Retourne la représentation sous forme de chaîne de caractères du rectangle"""

        return "[Rectangle] {}/{}".format(self.width, self.height)
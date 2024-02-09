#!/usr/bin/python3
"""Unittest for Rectangle class
"""


import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittest for Rectangle class"""

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_perimeter(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.perimeter(), 18)

    def test_str(self):
        rect = Rectangle(4, 5)
        self.assertEqual(str(rect), "####\n####\n####\n####\n####")

    def test_repr(self):
        rect = Rectangle(4, 5)
        self.assertEqual(repr(rect), "Rectangle(4, 5)")

    def test_set_width(self):
        rect = Rectangle(4, 5)
        rect.width = 6
        self.assertEqual(rect.width, 6)

    def test_set_height(self):
        rect = Rectangle(4, 5)
        rect.height = 6
        self.assertEqual(rect.height, 6)

    def test_get_number_of_instances(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(2, 3)
        self.assertEqual(rect1.get_number_of_instances(), 2)

    def test_bigger_or_equal(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(2, 3)
        self.assertEqual(Rectangle.bigger_or_equal(rect1, rect2), rect1)
        rect3 = Rectangle(6, 7)
        self.assertEqual(Rectangle.bigger_or_equal(rect3, rect1), rect3)

    def test_square(self):
        square = Rectangle.square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)


if __name__ == "__main__":
    unittest.main()
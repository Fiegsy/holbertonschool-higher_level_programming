#!/usr/bin/python3
"""
Module for testing the Rectangle subclass.
"""

import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleAttribut(unittest.TestCase):
    """Tests for attribute types of Rectangle class."""

    def test_width_type(self):
        """Test type of width attribute."""
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.width) is int)

    def test_height_type(self):
        """Test type of height attribute."""
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.height) is int)

    def test_x_type(self):
        """Test type of x attribute."""
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.x) is int)

    def test_y_type(self):
        """Test type of y attribute."""
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.y) is int)


class TestRectangleAttributeRaise(unittest.TestCase):
    """Tests for raising exceptions on attribute assignment."""

    def test_width_type_error(self):
        """Test TypeError on width not being int."""
        with self.assertRaises(TypeError):
            rect2 = Rectangle('2', 8, 1, 2)

    def test_width_value_error_negative(self):
        """Test ValueError on width being negative."""
        with self.assertRaises(ValueError):
            rect3 = Rectangle(-2, 8, 0, 0)

    def test_width_value_error_zero(self):
        """Test ValueError on width being zero."""
        with self.assertRaises(ValueError):
            rect3 = Rectangle(0, 8, 0, 0)

    # Similar tests for other attributes omitted for brevity...


class TestRectangleMethod(unittest.TestCase):
    """Tests for methods of Rectangle class."""

    @staticmethod
    def capture_output(rect, method):
        """Capture and return text printed in stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Tests for other methods omitted for brevity...

class TestBaseCreate(unittest.TestCase):
    """Tests for the create method of Base class."""

    def test_create_rectangle(self):
        """Test creating a rectangle."""
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertEqual("[Rectangle] (14) 14/14 - 14/14", str(rect14))

    # Additional tests omitted for brevity...

class TestBaseMethodWithFile(unittest.TestCase):
    """Tests for methods of Base class involving file I/O."""

    @classmethod
    def tearDown(cls):
        """Delete files after tests."""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass

    # Tests for other methods omitted for brevity...

if __name__ == '__main__':
    unittest.main()

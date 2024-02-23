#!/usr/bin/python3
"""Rectangle class unit tests"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_create_rectangle_with_width_and_height(self):
        Rectangle(1, 2)

    def test_create_rectangle_with_width_height_and_x(self):
        Rectangle(1, 2, 3)

    def test_create_rectangle_with_width_height_x_and_y(self):
        Rectangle(1, 2, 3, 4)

    def test_create_rectangle_invalid_width_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("1", 2)
        self.assertTrue('width must be an integer' in str(context.exception))

    def test_create_rectangle_invalid_height_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, "2")
        self.assertTrue('height must be an integer' in str(context.exception))

    def test_create_rectangle_invalid_x_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 2, "3")
        self.assertTrue('x must be an integer' in str(context.exception))

    def test_create_rectangle_invalid_y_string(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 2, 3, "4")
        self.assertTrue('y must be an integer' in str(context.exception))

    def test_create_rectangle_with_width_height_x_y_and_id(self):
        Rectangle(1, 2, 3, 4, 5)

    def test_create_rectangle_negative_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(-1, 2)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_rectangle_negative_height(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, -2)
        self.assertTrue('height must be > 0' in str(context.exception))

    def test_create_rectangle_zero_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_rectangle_zero_height(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 0)
        self.assertTrue('height must be > 0' in str(context.exception))

    def test_create_rectangle_negative_x(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 2, -3)
        self.assertTrue('x must be >= 0' in str(context.exception))

    def test_create_rectangle_negative_y(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 2, 3, -4)
        self.assertTrue('y must be >= 0' in str(context.exception))

    def test_create_rectangle_dictionary_with_width_and_height(self):
        Rectangle.create(**{'width': 2, 'height': 3})

    def test_create_rectangle_dictionary_with_width_height_and_x(self):
        Rectangle.create(**{'width': 2, 'height': 3, 'x': 12})

    def test_create_rectangle_dictionary_with_width_height_x_and_y(self):
        Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1})

    def test_create_rectangle_dictionary_with_width_height_x_y_and_id(self):
        Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89})

    def test_load_rectangle_from_file(self):
        Rectangle.load_from_file()

    def test_save_rectangle_to_file(self):
        r1 = Rectangle(8, 65, 2, 10, 2)
        r2 = Rectangle(10, 2, 1, 3, 5)
        Rectangle.save_to_file([r1, r2])

    def test_save_rectangle_to_file_empty_list(self):
        Rectangle.save_to_file([])

    def test_save_rectangle_to_file_with_None(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        dt.save_to_file(None)

    def test_rectangle_to_dictionary(self):
        with self.assertRaises(AttributeError) as context:
            Rectangle.to_dictionary(self)
        self.assertTrue("'TestRectangle' object has no attribute 'width'" in str(context.exception))

    def test_rectangle_area(self):
        dt = Rectangle(10, 10)
        dt.area()

    def test_rectangle_display(self):
        dt = Rectangle(1, 1)
        dt.display()

    def test_rectangle_area_with_specified_values(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(dt.area(), 2)

    def test_rectangle_string_representation(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(dt), '[Rectangle] (5) 3/4 - 1/2')

    def test_rectangle_display_with_specified_values(self):
        dt = Rectangle(1, 2, 3)
        dt.display()

    def test_rectangle_display_with_default_values(self):
        dt = Rectangle(1, 2)
        dt.display()


if __name__ == '__main__':
    unittest.main()

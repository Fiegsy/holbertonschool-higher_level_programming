#!/usr/bin/python3
"""Rectanglecl test"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_create_rectangle_with_width_and_height(self):
        Rectangle(1, 2)

    def test_create_rectangle_with_width_height_and_x_coordinate(self):
        Rectangle(1, 2, 3)

    def test_create_rectangle_with_width_height_x_and_y_coordinates(self):
        Rectangle(1, 2, 3, 4)

    def test_create_rectangle_with_non_integer_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("1", 2)
        self.assertTrue('width must be an integer' in str(context.exception))

    def test_create_rectangle_with_non_integer_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, "2")
        self.assertTrue('height must be an integer' in str(context.exception))

    def test_create_rectangle_with_non_integer_x_coordinate(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 2, "3")
        self.assertTrue('x must be an integer' in str(context.exception))

    def test_create_rectangle_with_non_integer_y_coordinate(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 2, 3, "4")
        self.assertTrue('y must be an integer' in str(context.exception))

    def test_create_rectangle_with_all_arguments_and_extra_argument(self):
        Rectangle(1, 2, 3, 4, 5)

    def test_create_rectangle_with_negative_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(-1, 2)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_rectangle_with_negative_height(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, -2)
        self.assertTrue('height must be > 0' in str(context.exception))

    def test_create_rectangle_with_zero_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_rectangle_with_zero_height(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 0)
        self.assertTrue('height must be > 0' in str(context.exception))

    def test_create_rectangle_with_negative_x_coordinate(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 2, -3)
        self.assertTrue('x must be >= 0' in str(context.exception))

    def test_create_rectangle_with_negative_y_coordinate(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 2, 3, -4)
        self.assertTrue('y must be >= 0' in str(context.exception))

    def test_create_rectangle_from_dictionary_with_width_and_height(self):
        Rectangle.create(**{'width': 2, 'height': 3})

    def test_create_rectangle_from_dictionary_with_width_height_and_x_coordinate(self):
        Rectangle.create(**{'width': 2, 'height': 3, 'x': 12})

    def test_create_rectangle_from_dictionary_with_all_arguments(self):
        Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1})

    def test_create_rectangle_from_dictionary_with_all_arguments_and_id(self):
        Rectangle.create(**{'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89})

    def test_load_rectangle_from_file(self):
        Rectangle.load_from_file()

    def test_save_to_file_with_empty_list(self):
        Rectangle.save_to_file([])

    def test_save_to_file_with_None(self):
        Rectangle.save_to_file(None)

    def test_save_to_file_with_list_of_rectangles(self):
        r1 = Rectangle(8, 65, 2, 10, 2)
        r2 = Rectangle(10, 2, 1, 3, 5)
        Rectangle.save_to_file([r1, r2])

    def test_save_to_file_with_empty_rectangle_list(self):
        Rectangle.save_to_file([])

    def test_save_to_file_with_None_rectangle(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        dt.save_to_file(None)

    def test_to_dictionary_with_invalid_object(self):
        with self.assertRaises(AttributeError) as context:
            Rectangle.to_dictionary(self)
        self.assertTrue("'TestRectangle' object has no attribute 'width'" in str(context.exception))

    def test_area_method(self):
        dt = Rectangle(10, 10)
        dt.area()

    def test_display_method(self):
        dt = Rectangle(1, 1)
        dt.display()

    def test_save_to_file_with_None_argument(self):
        Rectangle.save_to_file(None)

    def test_area_method_with_specific_rectangle(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(dt.area(), 2)

    def test_str_representation_of_rectangle(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(dt), '[Rectangle] (5) 3/4 - 1/2')

    def test_display_method_with_specific_rectangle(self):
        dt = Rectangle(1, 2, 3, 4)
        dt.display()

    def test_display_method_with_specific_rectangle_and_missing_arguments(self):
        dt = Rectangle(1, 2, 3)
        dt.display()

    def test_display_method_with_specific_rectangle_and_only_width_and_height(self):
        dt = Rectangle(1, 2)
        dt.display()

if __name__ == '__main__':
    unittest.main()

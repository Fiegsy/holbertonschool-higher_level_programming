#!/usr/bin/python3
"""Square test"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_create_square_with_side_length(self):
        Square(1)

    def test_create_square_with_side_length_and_x_coordinate(self):
        Square(1, 2)

    def test_create_square_with_side_length_x_and_y_coordinates(self):
        Square(1, 2, 3)

    def test_create_square_with_non_integer_side_length(self):
        with self.assertRaises(TypeError) as context:
            Square("1")
        self.assertTrue('width must be an integer' in str(context.exception))

    def test_create_square_with_non_integer_x_coordinate(self):
        with self.assertRaises(TypeError) as context:
            Square(1, "2")
        self.assertTrue('x must be an integer' in str(context.exception))

    def test_create_square_with_non_integer_y_coordinate(self):
        with self.assertRaises(TypeError) as context:
            Square(1, 2, "3")
        self.assertTrue('y must be an integer' in str(context.exception))

    def test_create_square_with_all_arguments_and_extra_argument(self):
        dt = Square(1, 2, 3, 4)
        self.assertTrue('[Square] (4) 2/3 - 1' in str(dt))

    def test_create_square_with_negative_side_length(self):
        with self.assertRaises(ValueError) as context:
            Square(-1)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_square_with_negative_x_coordinate(self):
        with self.assertRaises(ValueError) as context:
            Square(1, -2)
        self.assertTrue('x must be >= 0' in str(context.exception))

    def test_create_square_with_negative_y_coordinate(self):
        with self.assertRaises(ValueError) as context:
            Square(1, 2, -3)
        self.assertTrue('y must be >= 0' in str(context.exception))

    def test_create_square_with_zero_side_length(self):
        with self.assertRaises(ValueError) as context:
            Square(0)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_square_from_dictionary_with_only_size(self):
        Square.create(**{'size': 1})

    def test_create_square_from_dictionary_with_size_and_x_coordinate(self):
        Square.create(**{'size': 1, 'x': 2})

    def test_create_square_from_dictionary_with_all_arguments(self):
        Square.create(**{'size': 1, 'x': 2, 'y': 3, 'id': 89})

    def test_load_square_from_file(self):
        Square.load_from_file()

    def test_save_to_file_with_None(self):
        Square.save_to_file(None)

    def test_save_to_file_with_empty_list(self):
        Square.save_to_file([])

    def test_save_to_file_with_list_of_squares(self):
        Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])

    def test_save_to_file_with_None_argument(self):
        Square.save_to_file(None)

    def test_save_to_file_with_empty_square_list(self):
        Square.save_to_file([])

    def test_save_to_file_with_None_square(self):
        Square(1).save_to_file(None)

    def test_to_dictionary_with_invalid_object(self):
        with self.assertRaises(AttributeError) as context:
            Square.to_dictionary(self)
        self.assertTrue("'TestSquare' object has no attribute 'width'" in str(context.exception))

    def test_str_representation_of_square(self):
        self.assertEqual(str(Square(1, 2, 3, 4)), '[Square] (4) 2/3 - 1')

    def test_display_method_with_square(self):
        Square(1, 2, 3).display()

if __name__ == '__main__':
    unittest.main()

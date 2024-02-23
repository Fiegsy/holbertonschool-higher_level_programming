#!/usr/bin/python3
"""Square class unit tests"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_create_square_with_size(self):
        Square(1)

    def test_create_square_with_size_and_x(self):
        Square(1, 2)

    def test_create_square_with_size_x_and_y(self):
        Square(1, 2, 3)

    def test_create_square_invalid_size_string(self):
        with self.assertRaises(TypeError) as context:
            Square("1")
        self.assertTrue('width must be an integer' in str(context.exception))

    def test_create_square_invalid_x_string(self):
        with self.assertRaises(TypeError) as context:
            Square(1, "2")
        self.assertTrue('x must be an integer' in str(context.exception))

    def test_create_square_invalid_y_string(self):
        with self.assertRaises(TypeError) as context:
            Square(1, 2, "3")
        self.assertTrue('y must be an integer' in str(context.exception))

    def test_square_to_string_representation(self):
        dt = Square(1, 2, 3, 4)
        self.assertTrue('[Square] (4) 2/3 - 1' in str(dt))

    def test_create_square_negative_size(self):
        with self.assertRaises(ValueError) as context:
            Square(-1)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_square_negative_x(self):
        with self.assertRaises(ValueError) as context:
            Square(1, -2)
        self.assertTrue('x must be >= 0' in str(context.exception))

    def test_create_square_negative_y(self):
        with self.assertRaises(ValueError) as context:
            Square(1, 2, -3)
        self.assertTrue('y must be >= 0' in str(context.exception))

    def test_create_square_zero_size(self):
        with self.assertRaises(ValueError) as context:
            Square(0)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_create_square_dictionary_with_id(self):
        Square.create(**{'id': 89})

    def test_create_square_dictionary_with_id_and_size(self):
        Square.create(**{'id': 89, 'size': 1})

    def test_create_square_dictionary_with_id_size_and_x(self):
        Square.create(**{'id': 89, 'size': 1, 'x': 2})

    def test_create_square_dictionary_with_id_size_x_and_y(self):
        Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})

    def test_save_square_to_file_none(self):
        Square.save_to_file(None)

    def test_save_square_to_file_empty_list(self):
        Square.save_to_file([])

    def test_save_square_to_file_list_with_one_square(self):
        Square.save_to_file([Square(1)])

    def test_load_square_from_file(self):
        Square.load_from_file()

    def test_square_to_string_representation(self):
        with self.assertRaises(AttributeError) as context:
            Square.__str__(self)
        self.assertTrue("'TestSquare' object has no attribute 'x'" in str(context.exception))

    def test_square_to_dictionary(self):
        with self.assertRaises(AttributeError) as context:
            Square.to_dictionary(self)
        self.assertTrue("'TestSquare' object has no attribute 'width'" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
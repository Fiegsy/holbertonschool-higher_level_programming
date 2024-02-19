#!/usr/bin/python3
"""
Module of test of subclass Rectangle
"""

import unittest
import os
from pathlib import Path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareAttributes(unittest.TestCase):
    """Tests on type and attributes of Square"""

    def test_size_type(self):
        """Test if size is of type int"""
        sq1 = Square(2)
        self.assertIsInstance(sq1.size, int)
        self.assertEqual(sq1.width, 2)
        self.assertEqual(sq1.height, 2)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)

    def test_square_id_increment(self):
        """Test if the id of the square is incremented correctly"""
        sq3 = Square(8)
        sq4 = Square(12)
        self.assertEqual(sq3.id, sq4.id - 1)

    def test_square_with_two_args(self):
        """Test creation of square with size and x"""
        sq5 = Square(8, 2)
        sq6 = Square(12, 4)
        self.assertEqual(sq5.id, sq6.id - 1)
        self.assertEqual(sq5.x, 2)
        self.assertEqual(sq6.x, 4)

    def test_square_with_three_args(self):
        """Test creation of square with size, x, and y"""
        sq7 = Square(8, 2, 25)
        sq8 = Square(12, 4, 12)
        self.assertEqual(sq7.id, sq8.id - 1)
        self.assertEqual(sq7.x, 2)
        self.assertEqual(sq7.y, 25)
        self.assertEqual(sq8.x, 4)
        self.assertEqual(sq8.y, 12)

    def test_square_with_four_args(self):
        """Test creation of square with size, x, y, and id"""
        sq9 = Square(8, 2, 25, 8)
        sq10 = Square(12, 4, 16, 9)
        self.assertEqual(sq9.id, sq10.id - 1)
        self.assertEqual(sq9.x, 2)
        self.assertEqual(sq9.y, 25)
        self.assertEqual(sq9.id, 8)
        self.assertEqual(sq10.x, 4)
        self.assertEqual(sq10.y, 16)
        self.assertEqual(sq10.id, 9)

    def test_private_size_attribute(self):
        """Test if size is a private attribute"""
        sq11 = Square(10)


class TestSquareAttributeExceptions(unittest.TestCase):
    """Tests for attribute exceptions in Square"""

    def test_size_type_error(self):
        """Test if size raises TypeError when not int"""
        with self.assertRaises(TypeError):
            sq2 = Square('2')

    def test_size_value_error(self):
        """Test if size raises ValueError when negative"""
        with self.assertRaises(ValueError):
            sq3 = Square(-2)

    def test_size_zero_value_error(self):
        """Test if size raises ValueError when zero"""
        with self.assertRaises(ValueError):
            sq3 = Square(0)

    def test_square_no_args_error(self):
        """Test if Square raises TypeError with no args"""
        with self.assertRaises(TypeError):
            Square()

    def test_square_x_value_error(self):
        """Test if x raises ValueError when negative"""
        with self.assertRaises(ValueError):
            sq4 = Square(2, -8)

    def test_square_x_type_error(self):
        """Test if x raises TypeError when not int"""
        with self.assertRaises(TypeError):
            Square(2, "8")

    def test_square_y_value_error(self):
        """Test if y raises ValueError when negative"""
        with self.assertRaises(ValueError):
            sq4 = Square(2, 4, -8)

    def test_square_y_type_error(self):
        """Test if y raises TypeError when not int"""
        with self.assertRaises(TypeError):
            rsq5 = Square(2, 8, "5")

    def test_square_five_args_error(self):
        """Test if Square raises TypeError with five args"""
        with self.assertRaises(TypeError):
            sq3 = Square(2, 3, 8, 2, 16)


class TestSquareInstance(unittest.TestCase):
    """Tests for Square instantiation"""

    def test_square_instance_base(self):
        """Test if Square is an instance of Base"""
        self.assertIsInstance(Square(2), Base)

    def test_square_instance_rectangle(self):
        """Test if Square is an instance of Rectangle"""
        self.assertIsInstance(Square(2), Rectangle)

    def test_square_instance_square(self):
        """Test if Square is an instance of Square"""
        self.assertIsInstance(Square(2), Square)


class TestSquareMethods(unittest.TestCase):
    """Tests for Square methods"""

    def test_str_method(self):
        """Test str method"""
        sq12 = Square(2, 0, 5, 8)
        self.assertEqual(str(sq12), "[Square] (8) 0/5 - 2")

    def test_to_dictionary_method(self):
        """Test to_dictionary method"""
        sq13 = Square(8, 2, 1, 9)
        answer = {'size': 8, 'x': 2, 'y': 1, 'id': 9}
        self.assertDictEqual(answer, sq13.to_dictionary())

    def test_update_method_with_args(self):
        """Test update method with args"""
        sq14 = Square(1, 1, 1, 1)
        sq14.update(54, 12, 24, 8)
        self.assertEqual(str(sq14), "[Square] (54) 24/8 - 12")

    def test_update_method_with_kwargs(self):
        """Test update method with kwargs"""
        sq14 = Square(1, 1, 1, 1)
        sq14.update(**{"y": 54, "size": 2, "x": 8, "id": 8})
        self.assertEqual(str(sq14), "[Square] (8) 8/54 - 2")


class TestBaseMethods(unittest.TestCase):
    """Tests for Base methods"""

    def test_create_square_method(self):
        """Test create square method"""
        sq15 = Square(15, 15, 15, 15)
        sq15_dict = sq15.to_dictionary()
        sq15 = Square.create(**sq15_dict)
        self.assertEqual(str(sq15), "[Square] (15) 15/15 - 15")


class TestBaseMethodsWithFile(unittest.TestCase):
    """Tests for Base methods with file"""

    @classmethod
    def tearDownClass(cls):
        """Delete created files"""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass

    def test_save_to_file_empty(self):
        """Test save to file with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_none(self):
        """Test save to file with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_one_square(self):
        """Test save to file with one square"""
        sq17 = Square(12, 6, 2, 4)
        Square.save_to_file([sq17])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

    def test_save_to_file_two_squares(self):
        """Test save to file with two squares"""
        sq17 = Square(12, 6, 2, 4)
        sq18 = Square(48, 16, 8, 25)
        Square.save_to_file([sq17, sq18])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 80)

    def test_save_to_file_empty_list(self):
        """Test save to file with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file_no_file(self):
        """Test load from file when file doesn't exist"""
        answer = Square.load_from_file()
        path = Path('Square.json')
        self.assertFalse(path.is_file())

    def test_load_from_file_existing_file(self):
        """Test load from file when file exists"""
        sq17 = Square(12, 6, 2, 4)
        sq18 = Square(48, 16, 8, 25)
        Square.save_to_file([sq17, sq18])
        answer = Square.load_from_file()
        self.assertTrue(all(isinstance(form, Square) for form in answer))


if __name__ == '__main__':
    unittest.main()

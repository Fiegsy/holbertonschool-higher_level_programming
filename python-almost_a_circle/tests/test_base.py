#!/usr/bin/python3
"""Base class unit tests"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_base_instance_with_default_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_create_base_instance_with_incremented_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_create_base_instance_with_custom_id(self):
        b1 = Base(100000)
        self.assertEqual(b1.id, 100000)

    def test_create_base_instance_with_float_id(self):
        b1 = Base(1.1)
        self.assertEqual(b1.id, 1.1)

    def test_to_json_string_with_empty_list(self):
        Base.to_json_string([])

    def test_save_to_file_with_empty_list(self):
        Base.save_to_file([])

    def test_save_to_file_with_None(self):
        Base.save_to_file(None)

    def test_to_json_string_with_list_containing_dictionary(self):
        Base.to_json_string([{'id': 12}])

    def test_from_json_string_with_None(self):
        Base.from_json_string(None)

    def test_from_json_string_with_empty_string(self):
        Base.from_json_string("[]")

    def test_from_json_string_with_empty_list(self):
        Base.from_json_string("[]")

    def test_from_json_string_with_list_containing_dictionary(self):
        Base.from_json_string('[{"id": 89}]')

    def test_from_json_string_with_list_containing_dictionary_2(self):
        Base.from_json_string('[{"id": 89}]')


if __name__ == '__main__':
    unittest.main()

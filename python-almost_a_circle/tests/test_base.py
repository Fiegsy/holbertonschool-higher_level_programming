#!/usr/bin/python3
"""Base test"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_create_base_instance_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        
    def test_create_base_instance_without_id_again(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        
    def test_create_base_instance_with_custom_id(self):
        b1 = Base(100000)
        self.assertEqual(b1.id, 100000)

    def test_create_base_instance_with_float_id(self):
        b1 = Base(1.1)
        self.assertEqual(b1.id, 1.1)
        
    def test_convert_empty_list_to_json_string(self):
        Base.to_json_string([])

    def test_save_empty_list_to_file(self):
        Base.save_to_file([])

    def test_save_None_to_file(self):
        Base.save_to_file(None)

    def test_convert_empty_list_to_json_string_again(self):
        Base.to_json_string([])

    def test_convert_list_with_dictionary_to_json_string(self):
        Base.to_json_string([ { 'id': 12 }])

    def test_load_None_from_json_string(self):
        Base.from_json_string(None)

    def test_load_empty_list_from_json_string(self):
        Base.from_json_string("[]")

    def test_load_empty_list_from_json_string_again(self):
        Base.from_json_string("[]")

    def test_load_list_with_dictionary_from_json_string(self):
        Base.from_json_string('[{ "id": 89 }]')

    def test_load_list_with_dictionary_from_json_string_again(self):
        Base.from_json_string('[{ "id": 89 }]')

if __name__ == '__main__':
    unittest.main()


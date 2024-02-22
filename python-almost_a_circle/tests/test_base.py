#!/usr/bin/python3
"""Test cases for the Base class"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base_id_increment(self):
        """Test that Base class increments id correctly"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_base_custom_id(self):
        """Test creation of Base class with custom id"""
        base = Base(100000)
        self.assertEqual(base.id, 100000)

    def test_base_float_id(self):
        """Test creation of Base class with float id"""
        base = Base(1.1)
        self.assertEqual(base.id, 1.1)

    def test_to_json_string(self):
        """Test conversion of list to JSON string"""
        json_string = Base.to_json_string([{'id': 23}])
        self.assertEqual(json_string, '[{"id": 23}]')

    def test_from_json_string(self):
        """Test conversion of JSON string to list"""
        json_string = '[{"id": 89 }]'
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'id': 89}])

    def test_save_to_file(self):
        """Test saving list of dictionaries to file"""
        # Assuming a method to write to file is implemented
        Base.save_to_file([{'id': 1}, {'id': 2}])
        # Add assertions to check if file was created and contains correct data

    def test_save_
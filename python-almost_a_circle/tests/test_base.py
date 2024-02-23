#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_default_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        b1 = Base(100000)
        self.assertEqual(b1.id, 100000)

    def test_float_id(self):
        b1 = Base(1.1)
        self.assertEqual(b1.id, 1.1)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file_empty(self):
        Base.save_to_file([])

    def test_save_to_file_none(self):
        Base.save_to_file(None)

    def test_to_json_string_list(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertIsNone(Base.from_json_string(None))

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_single_item(self):
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])

if __name__ == '__main__':
    unittest.main()
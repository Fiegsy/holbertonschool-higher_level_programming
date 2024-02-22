#!/usr/bin/python3
"""Base class test"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_1(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_2(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_3(self):
        b = Base(100000)
        self.assertEqual(b.id, 100000)

    def test_4(self):
        b = Base(1.1)
        self.assertEqual(b.id, 1.1)

    def test_5(self):
        Base.to_json_string([None])

    def test_6(self):
        Base.to_json_string([])

    def test_7(self):
        Base.to_json_string(None)

    def test_9(self):
        Base.to_json_string("2")

    def test_10(self):
        Base.to_json_string([])

    def test_11(self):
        Base.to_json_string([{'id': 23}])

    def test_12(self):
        Base.save_to_file(None)

    def test_13(self):
        Base.save_to_file({})

    def test_14(self):
        Base.save_to_file({})

    def test_15(self):
        Base.from_json_string("[]")

    def test_16(self):
        Base.from_json_string([])

    def test_17(self):
        Base.from_json_string(None)

    def test_18(self):
        Base.from_json_string('[{ "id": 89 }]')

    if __name__ == '__main__':
        unittest.main()
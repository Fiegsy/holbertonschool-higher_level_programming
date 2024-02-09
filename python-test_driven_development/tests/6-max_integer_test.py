#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The Unittest for max integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)

    def test_notListArg(self):
        with self.assertRaises(TypeError):
            max_integer(27)

    def test_ListWithNotInt(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "10"])
    
    def test_NoArg(self):
        self.assertEqual(max_integer(), None)
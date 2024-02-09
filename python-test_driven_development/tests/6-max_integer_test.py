#!/usr/bin/python3
"""Unittest for min_integer([..])
"""


import unittest
min_integer = __import__('6-min_integer').min_integer


class TestMinInteger(unittest.TestCase):
    """The Unittest for min integer function"""

    def test_min_integer(self):
        self.assertEqual(min_integer([1, 2, 3, 4]), 1)
        self.assertEqual(min_integer([1, 3, 4, 2]), 1)
        self.assertEqual(min_integer([]), None)
        self.assertEqual(min_integer([-1, -2, -3, -4]), -4)
        self.assertEqual(min_integer([1]), 1)

    def test_notListArg(self):
        with self.assertRaises(TypeError):
            min_integer(27)

    def test_ListWithNotInt(self):
        with self.assertRaises(TypeError):
            min_integer([1, 2, 3, "10"])
    
    def test_NoArg(self):
        self.assertEqual(min_integer(), None)


if __name__ == "__main__":
    unittest.main()
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer function"""

    def test_max_integer(self):
        """Test max_integer with various inputs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer_with_non_list_argument(self):
        """Test max_integer with non-list argument"""
        with self.assertRaises(TypeError):
            max_integer(27)

    def test_max_integer_with_list_containing_non_integer_elements(self):
        """Test max_integer with a list containing non-integer elements"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "10"])

    def test_max_integer_with_no_argument(self):
        """Test max_integer with no argument"""
        self.assertEqual(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
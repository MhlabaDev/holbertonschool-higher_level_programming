#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with max value at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_max_at_end(self):
        """Test a list with max value at the end."""
        max_at_end = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_at_end), 4)

    def test_max_in_middle(self):
        """Test a list with max value in the middle."""
        max_in_middle = [1, 3, 4, 2, 1]
        self.assertEqual(max_integer(max_in_middle), 4)

    def test_one_negative_number(self):
        """Test a list with one negative number."""
        one_negative = [1, 2, -3, 4]
        self.assertEqual(max_integer(one_negative), 4)

    def test_only_negative_numbers(self):
        """Test a list with only negative numbers."""
        only_negative = [-1, -5, -3, -2]
        self.assertEqual(max_integer(only_negative), -1)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)


if __name__ == "__main__":
    unittest.main()

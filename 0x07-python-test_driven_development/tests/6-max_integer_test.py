#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unittest class """
    def test_for_int(self):
        """test function for list of integers
        """
        int_list = [2, 10, 3]
        self.assertEqual(max_integer(int_list), 10)

    def test_empty(self):
        """test for empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        """test for list of negative ints
        """
        self.assertEqual(max_integer([-2, -4, -10]), -2)

    def test_one_element(self):
        """test for only one element in list
        """
        self.assertEqual(max_integer([100]), 100)

    def test_equal_elements(self):
        """test for equal elements
        """
        self.assertEqual(max_integer([4, 4, 3]), 4)

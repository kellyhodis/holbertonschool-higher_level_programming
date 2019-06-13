#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest class
    """
    def test___init(self):
        """test for __init__ method
        """
        # test the id counter
        s = Base()
        self.assertEqual(s.id, 1)
        t = Base()
        self.assertEqual(t.id, 2)
        s.id = 2
        self.assertEqual(s.id, 2)

    def test_to_json_string(self):
        """test for to_json_string method
        """
        s = Base()

        # test return type of method
        S = s.to_json_string([])
        self.assertIsInstance(S, str)

    def test_save_to_file(self):
        """test for save_to_file method
        """

    def test_from_json_string(self):
        """test for from_json_string method
        """

    def test_create(self):
        """test for create method
        """

    def test_load_from_file(self):
        """test for load_from_file method
        """

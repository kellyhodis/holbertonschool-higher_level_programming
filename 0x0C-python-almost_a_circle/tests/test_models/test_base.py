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

        # test for empty string
        s = ""
        b = Base()
        l = b.from_json_string(s)
        self.assertTrue(len(l) is 0)
        self.assertIsInstance(l, list)

        # test for None parameter
        a = None
        m = b.from_json_string(a)
        self.assertTrue(len(m) is 0)
        self.assertIsInstance(m, list)

        # test for string = "[]"
        c = "[]"
        n = b.from_json_string(c)
        self.assertTrue(len(n) is 0)
        self.assertIsInstance(n, list)

        # test for specific JSON representation
        o = b.from_json_string('[{"id": 34}]')
        self.assertIsInstance(o, list)
        self.assertTrue(len(o) > 0)
        self.assertEqual(type(o[0]).__name__, "dict")

    def test_create(self):
        """test for create method
        """
        from models.rectangle import Rectangle
        s = Rectangle(1, 1)

        # test return type of method
        dict = {"id": 1}
        S = s.create(**dict)
        self.assertIsInstance(S, Base)

    def test_load_from_file(self):
        """test for load_from_file method
        """
        s = Base()

        # test return type of method
        S = s.load_from_file()
        self.assertIsInstance(S, list)

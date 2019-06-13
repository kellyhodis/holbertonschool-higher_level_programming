#!/usr/bin.python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unitest class
    """
    def test___init(self):
        """test for correct instance assignments
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

        # check that id increments with instances
        s = Rectangle(2, 4)
        self.assertEqual(s.id, r.id + 1)
        t = Rectangle(3, 3)
        self.assertEqual(t.id, s.id + 1)

        # check that id can be assigned
        u = Rectangle(5, 6, id=50)
        self.assertEqual(u.id, 50)

        # check that width cannot be 0 or a negative number
        with self.assertRaises(ValueError):
            v = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            w = Rectangle(0, 2)

        # check that height cannot be 0 or a negative number
        with self.assertRaises(ValueError):
            z = Rectangle(3, 0)
        with self.assertRaises(ValueError):
            a = Rectangle(3, -2)

        # check that width must be an integer
        with self.assertRaises(TypeError):
            b = Rectangle("b", 2)

        # check that height must be an integer
        with self.assertRaises(TypeError):
            c = Rectangle(3, "c")

        # check that x must be an integer
        with self.assertRaises(TypeError):
            d = Rectangle(1, 2, "d")

        # check that y must be an integer
        with self.assertRaises(TypeError):
            e = Rectangle(1, 2, 3, "e")

        # check that x cannot be < 0
        with self.assertRaises(ValueError):
            i = Rectangle(1, 2, -1)

        # check that y cannot be < 0
        with self.assertRaises(ValueError):
            j = Rectangle(1, 2, 3, -1)

        # check that id can be any type
        f = Rectangle(1, 2, id="f")
        g = Rectangle(2, 3, id=["a", "b", "c"])
        h = Rectangle(3, 4, id=(2, 3))

    def test_area(self):
        """test for area method
        """
        # check that area is correct value
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_display(self):
        """test for display method
        """
        # check for correct line count
        r = Rectangle(1, 2)

    def test_update(self):
        """test for update method
        """
        r = Rectangle(2, 5)
        self.assertTrue(r.width, 2)
        self.assertTrue(r.height, 5)

        # check that update works for values with list
        a = [8, 2, 4]
        r.update(a)
        self.assertTrue(r.width, 2)
        self.assertTrue(r.height, 4)
        self.assertTrue(r.id, 8)

        # check that update works for values with dictionary

    def test_to_dictionary(self):
        """test for to_dictionary method
        """

    def test___str(self):
        """test for __str__ method
        """

    def test_input_int(self):
        """test for input_int method
        """

    def test_wh_under_zero(self):
        """test for wh_under_zero method
        """

    def test_under_zero(self):
        """test for under_zero method
        """

    def test_width_getter(self):
        """test for width_getter
        """

    def test_width_setter(self):
        """test for width setter
        """

    def test_height_setter(self):
        """test for height setter
        """

    def test_x_getter(self):
        """test for x getter
        """

    def test_x_setter(self):
        """test for x setter
        """

    def test_y_getter(self):
        """test for y getter
        """

    def test_y_setter(self):
        """test for y setter
        """

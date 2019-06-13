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
        r.update(8, 3, 4, 5, 9)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 9)

        # check that update works for values with dictionary
        dict = {"id": 2, "width": 5, "x": 9, "height": 3, "y": 10}
        r.update(**dict)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_to_dictionary(self):
        """test for to_dictionary method
        """
        # test that dictionary has 5 attributes:
        # "id", "width", "height", "x", "y"
        r = Rectangle(12, 2)
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "width"))
        self.assertTrue(hasattr(r, "height"))
        self.assertTrue(hasattr(r, "x"))
        self.assertTrue(hasattr(r, "y"))
        R = r.to_dictionary()
        self.assertTrue("id" in R)
        self.assertTrue("width" in R)
        self.assertTrue("height" in R)
        self.assertTrue("x" in R)
        self.assertTrue("y" in R)

    def test___str(self):
        """test for __str__ method
        """
        # test that the str representation is correct
        r = Rectangle(7, 8)
        rstr = r.__str__
        """
        self.assertEqual(rstr.split(), ['[Rectangle]', '(' + r.id + ')',
                         r.x + '/' + r.y, '-', r.width + '/' + r.height])
        """

    def test_input_int(self):
        """test for input_int method
        """
        r = Rectangle(1, 1)

        # check that input must be an integer
        with self.assertRaises(TypeError):
            r.input_int("5", "height")

    def test_wh_under_zero(self):
        """test for wh_under_zero method
        """
        r = Rectangle(1, 1)

        # check that input must be >= 0 for width and height
        with self.assertRaises(ValueError):
            r.wh_under_zero(0, "width")
        with self.assertRaises(ValueError):
            r.wh_under_zero(-1, "width")

        with self.assertRaises(ValueError):
            r.wh_under_zero(0, "height")
        with self.assertRaises(ValueError):
            r.wh_under_zero(-1, "height")

    def test_under_zero(self):
        """test for under_zero method
        """
        # check that input must be >= 0 for x and y
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.under_zero(-2, "x")
        with self.assertRaises(ValueError):
            r.under_zero(-2, "y")

    def test_width_property_and_setter(self):
        """test for width_getter
        """
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.width = "r"
        with self.assertRaises(ValueError):
            r.width = -1
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_property_and_setter(self):
        """test for height setter
        """

        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.height = "r"
        with self.assertRaises(ValueError):
            r.height = -1
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_property_and_setter(self):
        """test for x setter
        """
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.x = "p"
        with self.assertRaises(ValueError):
            r.x = -3

    def test_y_property_and_setter(self):
        """test for y setter
        """
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.y = "x"
        with self.assertRaises(ValueError):
            r.y = -10

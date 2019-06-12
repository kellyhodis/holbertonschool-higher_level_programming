#!/usr/bin/python3
"""module that defines Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that defines a square and inherits from Rectangle
    """
    # class constructor
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """public methods
    """
    # override __str__
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    """properties and setters
    """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().input_int(value, "width")
        super().wh_under_zero(value, "width")
        self.width = value
        self.height = value

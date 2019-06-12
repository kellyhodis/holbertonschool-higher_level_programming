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

    # update class arguments
    def update(self, *args, **kwargs):
        try:
            self.id = args[0]
        except:
            for key, value in kwargs.items():
                if key is "id":
                    self.id = value
                if key is "size":
                    self.width = value
                    self.height = value
                if key is "x":
                    self.x = value
                if key is "y":
                    self.y = value
        else:
            try:
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass

    # return dictionary representation of Square
    def to_dictionary(self):
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

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

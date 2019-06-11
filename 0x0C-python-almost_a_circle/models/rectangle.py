#!/usr/bin/python3
"""module for Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from Base
    """
    # class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """public methods
    """
    # returns area of rectangle
    def area(self):
        return self.__width * self.__height

    # prints rectangle in stdout
    def display(self):
        for i in range(0, self.__y):
            print()
        for k in range(0, self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    # override __str__ method
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    """error checking methods
    """
    # check if value is int
    def input_int(self, input, attr):
        if type(input) is not int:
            raise TypeError("{} must be an integer".format(attr))

    # check if int is <= 0
    # for width and height
    def wh_under_zero(self, input, attr):
        if input <= 0:
            raise ValueError("{} must be > 0".format(attr))

    # check if int is < 0
    def under_zero(self, input, attr):
        if input < 0:
            raise ValueError("{} must be >= 0".format(attr))

    """properties and setters
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.input_int(value, "width")
        self.wh_under_zero(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.input_int(value, "height")
        self.wh_under_zero(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.input_int(value, "x")
        self.under_zero(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.input_int(value, "y")
        self.under_zero(value, "y")
        self.__y = value

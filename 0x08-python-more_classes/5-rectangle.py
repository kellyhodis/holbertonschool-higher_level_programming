#!/usr/bin/python3
"""
module that defines a rectangle
"""


class Rectangle:
    """Rectangle class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        string = ""
        for j in range(0, self.height):
            for i in range(0, self.width):
                string += "#"
            if j < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle(%d, %d)" % (self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

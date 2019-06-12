#!/usr/bin/python3
"""module for Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """public methods
    """
    # returns area of rectangle
    def area(self):
        """finds area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """prints rectangle in stdout
        """
        for i in range(0, self.__y):
            print()
        for k in range(0, self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    def update(self, *args, **kwargs):
        """assigns argument to each attribute
        """
        try:
            self.id = args[0]
        except:
            for key, value in kwargs.items():
                if key is "id":
                    self.id = value
                if key is "width":
                    self.__width = value
                if key is "height":
                    self.__height = value
                if key is "x":
                    self.__x = value
                if key is "y":
                    self.__y = value
        else:
            try:
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except:
                pass

    def to_dictionary(self):
        """return dictionary representation of Rectangle
        """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}

    def __str__(self):
        """override __str_ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    """error checking methods
    """
    def input_int(self, input, attr):
        """check if value is int
        """
        if type(input) is not int:
            raise TypeError("{} must be an integer".format(attr))

    def wh_under_zero(self, input, attr):
        """check if int is <= 0 for width and height
        """
        if input <= 0:
            raise ValueError("{} must be > 0".format(attr))

    def under_zero(self, input, attr):
        """check if int is < 0
        """
        if input < 0:
            raise ValueError("{} must be >= 0".format(attr))

    """properties and setters
    """
    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        """
        self.input_int(value, "width")
        self.wh_under_zero(value, "width")
        self.__width = value

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        """
        self.input_int(value, "height")
        self.wh_under_zero(value, "height")
        self.__height = value

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        """
        self.input_int(value, "x")
        self.under_zero(value, "x")
        self.__x = value

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        """
        self.input_int(value, "y")
        self.under_zero(value, "y")
        self.__y = value

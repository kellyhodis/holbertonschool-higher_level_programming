#!/usr/bin/python3
class MagicClass:

    def __init__(self, radius):
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self, 

#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for k in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ""
        else:
            p = ""
            for k in range(0, self.__position[1]):
                p += "\n"
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    p += " "
                p += "#" * self.__size
                p += "\n"
            p = p[:-1]
            return p

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or\
                len(value) != 2 or\
                type(value[0]) is not int or\
                type(value[1]) is not int or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

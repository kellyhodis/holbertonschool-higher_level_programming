#!/usr/bin/python3
"""
"""
def print_square(size):
    """
    Function that prints a square of length and width size
    """
    if type(size) is not int:
        if type(size) is not float or size < 0:
            raise TypeError("size must be an integer")
        size = int(size)
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)

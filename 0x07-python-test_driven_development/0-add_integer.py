#!/usr/bin/python3
"""
"""


def add_integer(a, b=98):
    """
    Integer addition function
    """
    if type(a) is not int or a is None:
        if type(a) is not float or a is None:
            raise TypeError("a must be an integer")
        a = int(a)
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
        b = int(b)
    if a + b == float('inf') or a + b == -float('inf'):
        return 0
    return a + b

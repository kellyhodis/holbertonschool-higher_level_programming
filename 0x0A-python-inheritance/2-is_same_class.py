#!/usr/bin/python3
"""module that checks for exact same object
"""


def is_same_class(obj, a_class):
    """function that returns True if object is exactly instance
    of specified class, otherwise return False
    """
    return type(obj) is a_class

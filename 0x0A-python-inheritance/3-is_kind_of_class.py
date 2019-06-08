#!/usr/bin/python3
"""module to check if same class or inherited from a class
"""


def is_kind_of_class(obj, a_class):
    """function that checks if an object is an instance of a class
    or an instance of class that inherited from specified class
    """
    if isinstance(obj, a_class) or type(obj) is a_class:
        return True

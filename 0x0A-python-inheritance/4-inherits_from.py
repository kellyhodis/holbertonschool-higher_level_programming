#!/usr/bin/python3
"""module that checks if object is only sub class
"""


def inherits_from(obj, a_class):
    """function that checks if object is instance of a class that
    inherited from the specified class
    """
    if isinstance(obj, a_class):
        return issubclass(type(obj), a_class)
    return False

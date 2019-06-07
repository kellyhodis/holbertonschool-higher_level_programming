#!/usr/bin/python3
"""module to define class MyList
"""


class MyList(list):
    """defines a class MyList
    that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))

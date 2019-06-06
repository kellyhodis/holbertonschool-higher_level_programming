#!/usr/bin/python3
"""module to count number of lines in a text file
"""


def number_of_lines(filename=""):
    """function to count and return number of lines in txt file
    """
    with open(filename) as file:
        i = -1
        for i, l in enumerate(file):
            pass
        return i + 1

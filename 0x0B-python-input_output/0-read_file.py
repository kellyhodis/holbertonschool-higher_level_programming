#!/usr/bin/python3
"""
module to read a file
"""


def read_file(filename=""):
    """function to read file
    """
    with open(filename) as file:
        contents = file.read()
    print(contents, end="")

#!/usr/bin/python3
"""
module to read a file
"""


def read_file(filename=""):
    """function to read file
    """
    f = open("my_file_0.txt", "r")
    if f.mode == 'r':
        contents = f.read()
    print(contents, end="")

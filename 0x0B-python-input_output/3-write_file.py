#!/usr/bin/python3
"""module to write string to text file
"""


def write_file(filename="", text=""):
    """function to write string to text file and return chars written
    """
    with open(filename, "w+") as file:
        count = file.write(text)
    return count

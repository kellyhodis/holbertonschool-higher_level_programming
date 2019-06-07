#!/usr/bin/python3
"""module to append to file
"""


def append_write(filename="", text=""):
    with open(filename, "a+") as file:
        count = file.write(text)
    return count

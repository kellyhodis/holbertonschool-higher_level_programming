#!/usr/bin/python3
"""module to read up to n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """function to read n lines of text and print to stdout
    """
    with open(filename) as file:
        for i, l in enumerate(file):
            if i < nb_lines or nb_lines <= 0:
                print(l, end="")

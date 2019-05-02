#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        char = "argument."
    elif len(argv) == 2:
        char = "argument:"
        number = 1
    else:
        char = "arguments:"
        number = 1
    print("{:d} {}".format(len(argv) - 1, char))
    for i in argv[1:]:
        print("{:d}: {}".format(number, i))
        number = number + 1

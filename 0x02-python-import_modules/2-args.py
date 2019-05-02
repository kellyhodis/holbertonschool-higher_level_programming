#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        char = ". "
    else:
        char = ": "
        number = 1
    print("{:d} arguments{}".format(len(argv) - 1, char))
    for i in argv[1:]:
        print("{:d}: {}".format(number, i))
        number = number + 1

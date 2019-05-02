#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    number = 0
    if len(argv) > 1:
        for i in argv[1:]:
            number = number + int(i)
    print("{:d}".format(number))

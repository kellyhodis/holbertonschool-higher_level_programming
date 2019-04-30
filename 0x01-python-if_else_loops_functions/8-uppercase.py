#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in str:
        length = length - 1
        spaces = ""
        if length == 0:
            spaces = "\n"
        if ord(i) > 96 and ord(i) < 123:
            print("{}".format(chr(ord(i) - 32)), end=spaces)
        else:
            print("{}".format(i), end=spaces)

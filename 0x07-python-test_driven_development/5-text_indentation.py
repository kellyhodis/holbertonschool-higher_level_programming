#!/usr/bin/python3
"""
"""
def text_indentation(text):
    """
    Text indentation function
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 1:
            if i == " ":
                continue
            else:
                flag = 0
        print("{}".format(i), end="")
        if i == ":" or i == "?" or i == ".":
            print("\n")
            flag = 1

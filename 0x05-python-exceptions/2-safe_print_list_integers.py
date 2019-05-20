#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            num += 1
            if num == x:
                break
        except (ValueError, TypeError):
            pass
    print()
    return num

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(0, list_length):
        try:
            div = my_list_1[index] / my_list_2[index]
            new_list.append(div)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return new_list

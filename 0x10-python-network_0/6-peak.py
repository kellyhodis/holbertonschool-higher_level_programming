#!/usr/bin/python3
"""Contains a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    '''Finds the peak in an unsorted list of integers.
    '''
    if list_of_integers:
        if len(list_of_integers) < 3:
            if len(list_of_integers) < 2:
                return (list_of_integers[0])
            else:
                if list_of_integers[0] > list_of_integers[1]:
                    return list_of_integers[0]
                else:
                    return list_of_integers[1]
        index = len(list_of_integers) // 2
        if list_of_integers[index - 1] <= list_of_integers[index]:
            if list_of_integers[index + 1] <= list_of_integers[index]:
                return list_of_integers[index]
            else:
                return find_peak(list_of_integers[index:])
        else:
            return find_peak(list_of_integers[:index])
    else:
        return None

#!/usr/bin/python3
"""Contains a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    '''Finds the peak in an unsorted list of integers.
    '''
    max = 0
    if list_of_integers:
        for int_ in list_of_integers:
            if int_ > max:
                max = int_
        return max
    else:
        return None

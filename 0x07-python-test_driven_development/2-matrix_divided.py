#!/usr/bin/python3
"""
"""

def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    length = -1
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if length == -1:
            length = len(row)
        else:
            if len(row) != length:
                raise TypeError("Each row of the matrix must have the same size")
            for column in row:
                if type(column) is not float and type(column) is not int:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    newmatrix = [[round(column / div, 2) for column in row] for row in matrix]
    return newmatrix

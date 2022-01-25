#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns a new matrix
    """
    val = len(matrix[0])
    mtx = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(0, len(matrix)):
        if val != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        mtx.append([])
        for j in matrix[i]:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
            result = round(j / div, 2)
            mtx[i].append(result)
    return mtx

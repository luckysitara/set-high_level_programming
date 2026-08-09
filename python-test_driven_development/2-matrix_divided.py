#!/usr/bin/python3
"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides a matrix
    """
    listError = 'matrix must be a matrix (list of lists) of integers/floats'
    sizeError = 'Each row of the matrix must have the same size'

    if type(matrix) is not list or not all(
            type(row) is list for row in matrix):
        raise TypeError(listError)

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError(listError)

    if len(matrix) > 0:
        row_len = len(matrix[0])
        for row in matrix:
            if len(row) != row_len:
                raise TypeError(sizeError)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item / div, 2) for item in row] for row in matrix]

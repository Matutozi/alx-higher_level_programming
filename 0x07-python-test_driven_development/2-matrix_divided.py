#!/usr/bin/python3
""" 2-matrix_divided: matrix_divided() """


def matrix_divided(matrix, div):
    """ 
    Function to divide all elements of a square matrix
    first arg: the matrix (matrix)
    second arg: the divisor (div)
    """
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if div is None:
        div = 1
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for element in matrix:
        if len(element) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for unit in element:
            if type(unit) not in [int]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix)
    r = 0
    while (r < row_len):
        c = 0
        while (c < len(matrix[0])):
            matrix[r][c] = (matrix[r][c]) / div
            c += 1
        r += 1


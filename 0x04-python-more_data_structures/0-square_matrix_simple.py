#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes square values of all integers of a matrix"""
    new_matrix = []
    nlist = []
    for i in range(len(matrix)):
        for elem in matrix[i]:
            nlist.append(elem ** 2)
        new_matrix.append(nlist)
        nlist = []
    return new_matrix

#!/usr/bin/python3
"""rotate 2d matrix by 90 degrees"""


def rotate_2d_matrix(matrix):
    """

    Args:
        matrix:  the 2-D matrix to be rotated by 90 deg clockwise

    Returns: Nothing

    """

    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for row in transpose:
        row.reverse()
    matrix.clear()
    matrix.extend(transpose)

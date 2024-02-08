#!/usr/bin/python3
"""empty module"""


def matrix_divided(matrix, div):
    """Function to divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists containing only integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, int) or isinstance(ele, float)
                    for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
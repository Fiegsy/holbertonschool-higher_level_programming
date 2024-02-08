#!/usr/bin/python3
"""Module with a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divivde all elements of matrix by div.

    Args:
        matrix (2D-list of integers): List of lists of integers or floats.
        div (int or float): Number to divide the elements of matrix by

    Returns:
        The new matrix containing all the divided elements.

    Raises:
        TypeError: if at least one element of the matrix or div is neither
        an int or float, or if the rows of matrix are not all the same size.
        ZeroDivisionError: If div is equal to zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    new = []
    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        elif len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        sub = []
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

            sub.append(round(ele / div, 2))

        new.append(sub)

    return new
#!/usr/bin/python3
"""Module with a Pascal triangle method"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]

    for line in range(n - 1):
        previous_row = triangle[-1]
        new_row = [1]
        for i in range(len(previous_row) - 1):
            new_num = previous_row[i] + previous_row[i + 1]
            new_row.append(new_num)

        if n >= 2:
            new_row.append(1)

        triangle.append(new_row)

    return triangle
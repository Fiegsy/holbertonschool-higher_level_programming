#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    if matrix is None:
        return None
    
    for row in matrix:
        print(" ".join(map(str, row)))

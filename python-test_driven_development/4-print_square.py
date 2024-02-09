#!/usr/bin/python3
"""Module that prints a square."""


def print_square(size):
    """Prints a square of a given size."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)


# Test cases
if __name__ == "__main__":
    try:
        print_square(-1)
    except ValueError as ve:
        print(ve)
    
    try:
        print_square('1')
    except TypeError as te:
        print(te)
    
    try:
        print_square(-1.5)
    except TypeError as te:
        print(te)
    
    try:
        print_square(None)
    except TypeError as te:
        print(te)
    
    try:
        print_square(["two"])
    except TypeError as te:
        print(te)
    
    try:
        print_square(1, 2)
    except TypeError as te:
        print(te)
    
    try:
        print_square()
    except TypeError as te:
        print(te)
    
    print_square(0)
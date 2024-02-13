#!/usr/bin/python3
"""Module with a function to read a file"""


def read_file(filename=""):
    """Reads a text file and prints its content"""

    with open(filename, 'r') as file:
        content = file.read()
        print(content)
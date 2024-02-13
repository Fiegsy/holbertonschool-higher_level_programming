#!/usr/bin/python3
"""Module with a function to write a string text into a file"""


def write_file(filename="", text=""):
    """Writes a string text into a file.

    Args:
        filename (str): Name of the file to write into.
        text (str): Text to write into the file.
    """

    with open(filename, 'w') as file:
        return file.write(text)
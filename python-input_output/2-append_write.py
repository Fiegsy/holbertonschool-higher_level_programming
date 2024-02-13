#!/usr/bin/python3
"""Module with a function to append a string text to a file"""


def append_write(filename="", text=""):
    """Appends a string text to a file.

    Args:
        filename (str): Name of the file to append to.
        text (str): Text to append to the file.
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
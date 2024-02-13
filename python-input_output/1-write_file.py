#!/usr/bin/python3
"""Module with a function to write to a file"""


def write_file(filename="", text=""):
    """Writes text to a file"""

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
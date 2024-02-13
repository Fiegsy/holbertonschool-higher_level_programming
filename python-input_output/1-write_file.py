#!/usr/bin/python3
"""Module with a function to write content to a file"""


def write_to_file(file_path="", data=""):
    """Writes data to a file.

    Args:
        file_path (str): The path to the file to write to.
        data (str): The data to write to the file.
    """

    with open(file_path, 'w') as file:
        return file.write(data)

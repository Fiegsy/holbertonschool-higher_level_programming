#!/usr/bin/python3
"""Module with a function to write content to a file"""


def write_to_file(filename="", content=""):
    """Writes content to a file. If the file does not exist, it creates one.

    Args:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.
    """

    with open(filename, 'w') as file:
        return file.write(content)
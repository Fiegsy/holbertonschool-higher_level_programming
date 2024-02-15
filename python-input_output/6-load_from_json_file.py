#!/usr/bin/python3
"""Module with a function to create an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON formatted text file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        The Python object represented by the JSON data in the file.
    """

    with open(filename, encoding="utf-8") as file:
        return json.load(file)
#!/usr/bin/python3
"""Module with a function to write an object to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a JSON formatted text file.

    Args:
        my_obj (any): Object to be written to the file as JSON.
        filename (str): Name of the file to write to.
    """

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
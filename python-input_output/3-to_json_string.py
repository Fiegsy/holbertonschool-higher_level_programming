#!/usr/bin/python3
"""Module JSON"""


import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON formatted string."""
    return json.dumps(my_obj)
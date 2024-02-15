#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    my_list = load_from_json_file('add_item.json')
    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, 'add_item.json')

except Exception:
    save_to_json_file(sys.argv[1:], 'add_item.json')
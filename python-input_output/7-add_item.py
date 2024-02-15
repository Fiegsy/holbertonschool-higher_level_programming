#!/usr/bin/python3
"""Import module JSON"""


import json
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(args)

save_to_json_file(my_list, filename)
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print(f"{key}: {value}") for key, value in sorted(a_dictionary.items())]

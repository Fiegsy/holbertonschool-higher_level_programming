#!/usr/bin/python3
"""Empty module"""


class MyList(list):
    """a function that inherits a list"""
    def print_sorted(self):
        """Prints the sorted list"""
        sorted_list = sorted(self)
        print("Sorted list:", sorted_list)
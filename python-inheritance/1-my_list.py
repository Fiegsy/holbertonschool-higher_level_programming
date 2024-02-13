#!/usr/bin/python3
"""Empty module"""


class MyList(list):
    """a function that inherits a list"""
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
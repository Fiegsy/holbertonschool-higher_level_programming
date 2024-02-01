#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for i in my_list:
            if len < x:
                print("{}".format(i), end="")
                len += 1
        print()
        return (len)
    except IndexError:
        print()

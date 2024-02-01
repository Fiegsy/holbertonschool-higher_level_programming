#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        inside_result = a / b
        print("Inside result: {}".format(inside_result))
    except ZeroDivisionError:
        inside_result = None
        print("Inside result: {}".format(inside_result))
    finally:
        return inside_result

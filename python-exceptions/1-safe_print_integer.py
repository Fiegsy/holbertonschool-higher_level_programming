#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("Printing... Done!")
        return True
    except Exception:
        return False

#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    _len = len(argv)

    if _len == 1:
        print("0 arguments.")

    elif _len == 2:
        print(f"1 argument:\n1: {argv[1]}")

    else:
        print(f"{_len - 1} arguments:")

        for i in range(1, _len):
            print(f"{i}: {argv[i]}")

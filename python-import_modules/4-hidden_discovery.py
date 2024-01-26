#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    [print(File) for File in dir(hidden_4) if not File.startswith("__")]


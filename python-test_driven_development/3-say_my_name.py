#!/usr/bin/python3
"""Module with a function that prints out its arguments in a sentence"""


def say_my_name(first_name, last_name=""):
    """Print out the name and last name passed as arguments in a sentence.

    Args:
        first_name (string): First name to print.
        last_name (string, optional): Last name to print. Defaults to "".

    Raises:
        TypeError: if either of the two arguments is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
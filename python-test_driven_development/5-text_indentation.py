#!/usr/bin/python3
"""Module with a function that indents a text"""


def text_indentation(text):
    """Indent a text by adding two new lines after specific separators.

    Args:
        text (str): Text to indent

    Raises:
        TypeError: if text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    sep = ".?:"
    new = ""
    mark = 0
    for i in range(len(text)):
        if text[i] in sep or i == len(text) - 1:
            new += (text[mark:i + 1]).strip() + "\n\n"
            if text[i] == " ":
                mark = i + 2
            else:
                mark = i + 1

    print(new.strip(), end="")
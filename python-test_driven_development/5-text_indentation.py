#!/usr/bin/python3
"""a module that defines the text_identation function"""


def text_indentation(text):
    """a function that print the content of a text

    returns: nothing

    raises:
        TypeError: if the text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sentence = ""
    for i in text:
        sentence += i
        if i in [".", "?", ":"]:
            print("{}\n".format(sentence.strip()))
            sentence = ""
    if sentence.strip() != "":
        print("{}".format(sentence.strip()), end="")
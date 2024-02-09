#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Indent a text by adding two new lines after specific separators.

    Args:
        text (str): Text to indent

    Raises:
        TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    indented_text = ""
    start_index = 0

    for index, char in enumerate(text):
        if char in separators or index == len(text) - 1:
            substring = text[start_index:index + 1].strip()
            indented_text += substring + "\n\n"
            start_index = index + 1 if char == " " else index

    print(indented_text.strip(), end="")


# Test cases
if __name__ == "__main__":
    try:
        text_indentation("Bonjour. Comment allez-vous? Dites cela: Hej.")
    except Exception as e:
        print(e)

    try:
        text_indentation(22)
    except Exception as e:
        print(e)

    try:
        text_indentation("")
    except Exception as e:
        print(e)

    try:
        text_indentation(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
            Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
            Non autem hoc: igitur ne illud quidem."""
        )
    except Exception as e:
        print(e)

    try:
        text_indentation()
    except Exception as e:
        print(e)

    try:
        text_indentation(
            """         Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
            Quonam modo?                   Utrum igitur tibi litteram videor an totas paginas commovere? \
            Non autem hoc: igitur ne illud quidem."""
        )
    except Exception as e:
        print(e)
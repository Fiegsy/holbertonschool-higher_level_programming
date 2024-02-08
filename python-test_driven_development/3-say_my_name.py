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

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    try:
        say_my_name("John", "Doe")
    except Exception as e:
        print(e)

    try:
        say_my_name("Jane")
    except Exception as e:
        print(e)

    try:
        say_my_name(123, "Smith")
    except Exception as e:
        print(e)

    try:
        say_my_name("Alex", 456)
    except Exception as e:
        print(e)
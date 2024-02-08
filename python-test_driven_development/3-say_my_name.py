def say_my_name(first_name, last_name=""):
    """Prints the first and last name in a sentence.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a string or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    try:
        say_my_name("John", "Smith")
        say_my_name("Walter", "White")
        say_my_name("Bob")
        say_my_name(12, "White")
    except TypeError as e:
        print(e)

    try:
        say_my_name(None)
    except TypeError as e:
        print(e)

    try:
        say_my_name(None, "poppins")
    except TypeError as e:
        print(e)

    try:
        say_my_name("mary", None)
    except TypeError as e:
        print(e)

    try:
        say_my_name(1, "Poppins")
    except TypeError as e:
        print(e)

    try:
        say_my_name("mary", 2)
    except TypeError as e:
        print(e)

    try:
        say_my_name(["mary"], "poppins")
    except TypeError as e:
        print(e)

    try:
        say_my_name("mary", ["poppins"])
    except TypeError as e:
        print(e)

    try:
        say_my_name()
    except TypeError as e:
        print(e)
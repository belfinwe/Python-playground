def is_number(in_data: str) -> tuple:
    """
    Takes a string, returns a tuple. Checks if input is an int or float.

    Returns one of the following tuples:
    (the_number, "int", True)
    (the_number, "float", True)
    (None, "Not a number", False)
    """
    try:
        i = int(in_data)
        return i, "int", True
    except ValueError:
        try:
            i = float(in_data)
            return i, "float", True
        except ValueError:
            return None, "Not a number", False


def is_number_mk2(num: str) -> tuple:
    """
    Takes a string, returns a tuple. Checks if input is an int or float.

    The difference from `is_number()`: this function uses `isinstance()` to check if int or float.
    Returns one of the following tuples:
    (the_number, "int", True)
    (the_number, "float", True)
    (None, "Not a number", False)
    """
    try:
        if isinstance(int(num), int):
            return int(num), "int", True
    except ValueError:
        try:
            if isinstance(float(num), float):
                return float(num), "float", True
        except ValueError:
            return None, "Not a number", False


if __name__ == "__main__":
    print("first")
    print(is_number("1"))
    print(is_number("1.0"))
    print(is_number("one"))

    print("\nmk2")
    print(is_number_mk2("1"))
    print(is_number_mk2("1.0"))
    print(is_number_mk2("one"))

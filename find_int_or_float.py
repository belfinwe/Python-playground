def is_number(indata: str) -> tuple:
    """
    Takes a string, returns a tuple. Checks if input is an int or float.

    Returns one of the following tuples:
    (the_number, "int", True)
    (the_number, "float", True)
    (None, "Not a number", False)
    """
    try:
        i = int(indata)
        return i, "int", True
    except:
        try:
            i = float(indata)
            return i, "float", True
        except:
            return None, "Not a number", False


if __name__ == "__main__":
    input_data = input("Write something: ")
    print(is_number(input_data))

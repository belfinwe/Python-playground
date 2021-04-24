def square(number: int):
    """
    Multiplies the number (int) with itself.
    """
    # if type(number) == int or type(number) == float:
    if isinstance(number, int) or isinstance(number, float):
        return number*number
    else:
        return "Only takes int or float."


def map_square(numbers_as_list: list) -> list:
    """
    Takes a list with ints, and returns a list with the double ints.
    """
    # Looks like maps takes a method/function, and then an iterator with values to be passed on to the method.
    square_numbers = map(square, numbers_as_list)
    return list(square_numbers)


def has_membership(person: str):
    if person in get_member_list():
        return True
    return False


def get_member_list():
    return ["Kate", "Bob", "Blackadder", "Mellchet", "Cpt. Darling"]


if __name__ == "__main__":
    # numbers = [1, 2, 3, 4, 5]
    # squared_numbers = list(map(square, numbers))
    print(f"144 fordoblet: {square(144)}")
    print(f"[144, 128] fordoblet: {map_square([144, 128])}")
    print(f"[12, 13, 14] fordoblet: {map_square([12, 13, 14])}")

    print(f"map of member list: {list(map(has_membership, ['Kate', 'Lizzy', 'Edmund']))}")

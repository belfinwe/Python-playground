"""
My decorator. Can be used on functions that handles only numbers.

May need some tweaking if used for use cases where more or less than two
nunbers are involved.
"""


def is_number(in_data: str) -> bool:
    """Returns True if input is int or float, otherwise returns False"""
    try:
        i = int(in_data)
        return True
    except ValueError:
        try:
            i = float(in_data)
            return True
        except ValueError:
            return False


def check_if_number(func):
    def wrapper(inn: tuple):
        assert len(inn) == 2, "Should only be two elements in tuple."
        res = list(map(is_number, inn))
        if False in res:
            raise ValueError
        return func(inn)
    return wrapper


@check_if_number
def add_up(inn: tuple) -> float:
    return float(inn[0] + inn[1])


if __name__ == "__main__":
    print(add_up((2,3)))  # Runs
    print(add_up((3,3)))  # Runs
    # print(add_up((4,3,5)))  # AssertionError, three elements instead of two
    # print(add_up(("two",3)))  # ValueError, string instead of int or float

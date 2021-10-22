# For importing from parent directory
import inspect
import os, sys, inspect
current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(current_directory)
parent_dir = os.path.dirname(current_directory)
print(parent_dir)
sys.path.insert(0, parent_dir) 

from decorators_pg_dir import my_decorator_pg


@my_decorator_pg.check_if_number
@my_decorator_pg.convert_to_num
def add_up(inn: tuple, stuff: str = "Not much") -> float:
    """Adds to given numbers"""
    return float(inn[0] + inn[1])


@my_decorator_pg.check_if_number
@my_decorator_pg.convert_to_num
def subtract(num_tuple: tuple) -> float:
    return float(num_tuple[0] - num_tuple[1])


if __name__ == "__main__":
    print(add_up((2,3), stuff="Meh"))  # Runs
    print(add_up((3,3)))  # Runs. But it seems that `stuff` is not present in args or kwargs in the wrapper.
    # print(add_up((4,3,5)))  # AssertionError, three elements instead of two
    # print(add_up(("two",3)))  # ValueError, string instead of int or float

    print(subtract((50, "15")))
    # print(subtract((100, 200, 300)))  # AssertionError, three elements instead of two
    # print(subtract(("500", "five")))  # ValueError, string instead of int or float

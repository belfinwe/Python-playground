# For importing from parent directory
import inspect
import os, sys, inspect
current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(current_directory)
parent_dir = os.path.dirname(current_directory)
print(parent_dir)
sys.path.insert(0, parent_dir) 
import find_int_or_float

"""
My decorator. Can be used on functions that handles only numbers.

May need some tweaking if used for use cases where more or less than two
numbers are involved.
"""


def check_if_number(func):
    """Wrapper that uses `is_number()` to check if the given arguments are indeed numbers."""
    def wrapper(*args, **kwargs):
        addition_tuple = args[0]
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        # To add clarity and add feedback in case of wrong doing. Will raise AssertionError if False.
        assert len(addition_tuple) == 2, "Should only be two elements in tuple!"  

        # Checks if arguments are numbers
        if False in list(map(find_int_or_float.is_number, addition_tuple)):  # If one of the elements is not a number, raise ValueError
            raise ValueError
        
        return func(addition_tuple)
    return wrapper


def convert_to_num(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            return func(tuple([find_int_or_float.is_number(i)[0] for i in args[0]]))
        return func(tuple([find_int_or_float.is_number(i)[0] for i in kwargs["num_tuple"]]))
        
    return wrapper

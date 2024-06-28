"""Store the decorates here"""
from functools import wraps
import logging

logg = logging.getLogger()

# decorator for checking if number is zero
def check_for_zero(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num1, num2 = args
        if num2 == 0:
            return None
        return func(num1, num2)
    return wrapper


def log_inputs(func):
    logging.info(f"{func.__name__=}")
    @wraps(func)
    def wrapper(*args, **kwargs):
        logg.info(f"args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

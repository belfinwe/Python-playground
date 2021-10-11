# https://medium.com/techtofreedom/7-levels-of-using-decorators-in-python-370473fcbe76
from functools import wraps


def add_author(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        author = "Some Author"
        return author + "\n" + func(*args, **kwargs)
    return wrapper


@add_author
def get_title(title: str):
    """A function that receives and returns a title."""
    return title

print(get_title.__name__)
print(get_title.__doc__)

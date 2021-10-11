from functools import wraps


def decorator_list(func):  # 3. func here is the the add_together function
    @wraps(func)
    def inner(list_of_tuples):
        return [func(val[0], val[1]) for val in list_of_tuples]  # 4. Loops through the given list of tuples, using the tuples as input to the add_together function
    return inner  # 5. Return the return value from inner(), i.e. the list of results


@decorator_list  # 2. Picks up the function call?
def add_together(a, b):
    """Due to decorators, takes a list of tuples. Each tuple can only have two elements!"""
    return a + b


print(f"{add_together.__name__}(): {add_together.__doc__}")

# 1. Calls the function add_together
print(add_together([(1,3),(4,9),(5,9)]))
print(add_together([(9,2)]))

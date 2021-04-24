"""
Construct an iterator from those elements of iterable for which `function` returns true.
`iterable` may be either a sequence, a container which supports iteration, or an iterator. If `function` is None,
the identity function is assumed, that is, all elements of iterable that are false are removed.
"""


def even(number):
    if (number % 2) == 0:
        return True
    return False


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(even, numbers))
    print(f"Even numbers: {even_numbers}")


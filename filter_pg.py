def even(number):
    if (number % 2) == 0:
        return True
    return False

numbers = [1,2,3,4,5]
even_numbers = list(filter(even, numbers))


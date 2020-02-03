def square(number: int):
    if type(number) == int or type(number) == float:
        return number*number
    else:
        return "Only takes int or float."


def map_square(numbers_as_list: list):
    square_numbers = map(square, numbers_as_list)
    return list(square_numbers)


if __name__ == "__main__":
    # numbers = [1, 2, 3, 4, 5]
    # squared_numbers = list(map(square, numbers))
    print(f"144 fordoblet: {square(144)}")
    print(f"[144, 128] fordoblet: {map_square([144, 128])}")


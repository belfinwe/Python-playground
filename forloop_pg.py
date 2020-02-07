def double_custom(in_data: int) -> int:
    return in_data * 2


if __name__ == "__main__":
    list_i = [10, 20, 30, 40, 50]
    print(list(double_custom(i) for i in list_i))
    # print(double(i) for i in list_i)  # Returns a generator object?
    print(list(map(double_custom, list_i)))

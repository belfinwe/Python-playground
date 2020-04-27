def double_custom(in_data: int) -> int:
    """
    Return double the input. Takes int as input.
    """
    return in_data * 2


def alter_list(inn: list):
    """
    Returns a new list with only half the items
    """
    res = [inn[i] for i in range(len(inn)) if i % 2 == 0]
    return res


if __name__ == "__main__":
    list_i = [10, 20, 30, 40, 50]
    print(list(double_custom(i) for i in list_i))
    # print(double(i) for i in list_i)  # Returns a generator object?
    print(list(map(double_custom, list_i)))
    print(alter_list(list_i))

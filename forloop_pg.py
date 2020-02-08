list_i = [10, 20, 30, 40, 50]


def double(in_data: int) -> int:
    return in_data * 2


def alter_list(inn: list):
    """
    Returns a new list with onyl half the items
    """
    res = [inn[i] for i in range(len(inn)) if i%2 == 0]
    return res



if __name__ == "__main__":
    print(list(double(i) for i in list_i))
    # print(double(i) for i in list_i)
    print(list(map(double, list_i)))
    print(alter_list(list_i))

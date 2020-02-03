list_i = [10, 20, 30, 40, 50]


def double(in_data: int) -> int:
    return in_data * 2


print(list(double(i) for i in list_i))
# print(double(i) for i in list_i)
print(list(map(double, list_i)))

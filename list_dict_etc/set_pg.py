import random


def testing_set(list_in: list) -> set:
    """
    Returns a set of the provided list
    """
    a = {i for i in list_in}
    return a


def random_item(list_in: list) -> str:
    """
    Provides a pseudo random item for the given list
    """
    j = random.randint(0, 5)
    return list_in[j]


def create_random_set(list_in: list) -> set:
    misc_set = {random_item(list_in) for i in range(10)}
    return misc_set


def create_random_list(list_in: list) -> list:
    misc_list = [random_item(list_in) for i in range(10)]
    return misc_list


if __name__ == "__main__":
    set_liste = ["Cheese", "Biscuit", "Sausage", "Wine", "Cheese", "Bread"]

    set_liste_res = testing_set(set_liste)
    print(set_liste_res)

    print("Set:")
    print(create_random_set(set_liste))

    print("List:")
    print(create_random_list(set_liste))



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
    j = random.randint(0, len(list_in) - 1)
    return list_in[j]


def create_random_set(list_in: list) -> set:
    misc_set = {random_item(list_in) for i in range(10)}
    return misc_set


def create_random_list(list_in: list) -> list:
    misc_list = [random_item(list_in) for i in range(10)]
    return misc_list


if __name__ == "__main__":
    set_liste = ["Cheese", "Biscuit", "Sausage", "Wine", "Cheese", "Bread"]
    print(f"listen som testes på: {set_liste}\nLengde: {len(set_liste)}")

    set_liste_res = testing_set(set_liste)
    print(f"testing_set: {set_liste_res}\nLengde: {len(set_liste_res)}")

    print(f"Set: {create_random_set(set_liste)}")

    print(f"List: {create_random_list(set_liste)}")

def testing_zip():
    iterator1 = ["a1", "b1", "c1"]
    iterator2 = ["a2", "b2", "c2"]
    iterator3 = ["a3", "b3", "c3"]
    iterator4 = ["a4", "b4", "c4", "d4"]
    # Ser ut som at zip i dei tilfelle her gjer om listene over til kvar sin tuple
    # og setter dei inn i ei overordnet liste/zip objekt der kvar tuple er eit element i den lista
    zipped_result = list(zip(iterator1, iterator2, iterator3))

    # print(zipped_result)
    return zipped_result


def omg():
    a = [1, 2]
    b = [3, 4]
    return list(zip(a, b))


def fjas():
    a = [1, 2]
    b = [3, 4]
    c = a + b
    return c


if __name__ == "__main__":
    print(f"testing_zip: {testing_zip()}")
    print(f"omg: {omg()}")
    print(f"fjas: {fjas()}")

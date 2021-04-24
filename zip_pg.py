def testing_zip():
    even_numbers = [2, 4]
    even_numbers_squared = [4, 8]
    # Ser ut som at zip i dei tilfelle her gjer om listene over til kvar sin tuple
    # og setter dei inn i ei overordnet liste der kvar tuple er eit element i den lista
    zipped_result = list(zip(even_numbers, even_numbers_squared))

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

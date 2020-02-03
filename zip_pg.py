def testing_zip():
    even_numbers = [2, 4]
    even_numbers_squared = [4, 8]
    zipped_result = list(zip(even_numbers, even_numbers_squared))

    print(zipped_result)
    return zipped_result


if __name__ == "__main__":
    testing_zip()

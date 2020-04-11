def walrus():
    for i in range(0, 5, 1):
        if (n := i+1) < 3:
            print(f"{n} er mindre enn 3")
        else:
            print(f"else: {n}")
    return f"n blei til slutt {n}"


def positional_only(a, /, b, *, c):
    """
    A er kun for posisjon.
    B kan være poisjonell eller med nøkkelord.
    C må være nøkkelord.
    """
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")
    return f"{a}, {b}, {c}"


if __name__ == "__main__":
    walrus()
    positional_only("Må være posisjonell", "Valgfri!", c="Må være med nøkkelord!")

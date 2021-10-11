from built_in_functions import filter_pg, map_pg, zip_pg


# Er litt usikker på om det er slik her det kan gjerast.
# Eller som ein skal gjere som eg har gjort i test_three_eight.py


def test_even():
    assert not filter_pg.even(5), f"Failed. Results should be False"
    assert not filter_pg.even(5), f"Failed. Should be False"
    assert filter_pg.even(6), f"Failed. Resultatet burde være True"


def test_zip():
    assert type(zip_pg.testing_zip()) == list, f"Failed, type should be list, but is {type(zip_pg.testing_zip())}"
    assert not type(zip_pg.testing_zip()) == dict, f"Failed, type should be dict, but is {type(zip_pg.testing_zip())}"


def test_square():
    sq = 3
    assert map_pg.square(sq) == 9, f"Failed, map_pg(3) should be 9, but is {map_pg.square(sq)}"
    liste_str_testing = ["144", "128"]
    assert map_pg.square(liste_str_testing) == "Only takes int or float.", \
        f"Should not be able to accept strings."


def test_map_square():
    liste_testing = [144, 128]
    assert map_pg.map_square(liste_testing) == [20736, 16384], \
        f"Failed, result was {map_pg.map_square(liste_testing)}, should have been [20736, 16384]"\
        f"Failed, results: {map_pg.map_square(liste_testing)}, should be [20736, 16384]"

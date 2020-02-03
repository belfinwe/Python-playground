import filter_pg
import zip_pg
import map_pg

# Er litt usikker på om det er slik her det kan gjerast.
# Eller som ein skal gjere som eg har gjort i test_three_eight.py


def test_even():
    assert not filter_pg.even(5), f"Feilet. Resultatet burde være False"
    assert filter_pg.even(6), f"Feilet. Resultatet burde være True"


def test_zip():
    assert type(zip_pg.testing_zip()) == list, f"Feilet, typen burde være liste, men er {type(zip_pg.testing_zip())}"
    assert not type(zip_pg.testing_zip()) == dict, f"Feilet, typen burde ikke være dict, men er {type(zip_pg.testing_zip())}"


def test_square():
    sq = 3
    assert map_pg.square(sq) == 9, f"Feilet, burde map_pg(3) burde være 9, men er {map_pg.square(sq)}"
    liste_str_testing = ["144", "128"]
    assert map_pg.square(liste_str_testing) == "Only takes int or float.", \
        f"Skal ikkje kunne ta imot str (på sikt berre ikkje bokstaver?)"


def test_map_square():
    liste_testing = [144, 128]
    assert map_pg.map_square(liste_testing) == [20736, 16384], \
        f"Feilet, resultatet blei {map_pg.map_square(liste_testing)}, skulle vært [20736, 16384]"

import pytest
import three_eight


def test_walrus():
    assert type(three_eight.walrus()) == str, f"Feilet, typen til walrus() er {type(three_eight.walrus())}"
    assert type(int(three_eight.walrus()[-1])) == int, f"Feilet, skal være ein int, er {type(int(three_eight.walrus()[-1]))}"


def test_positional_only():
    assert three_eight.positional_only("A", "B", c="C"), "Feilet. Er nok feil med inndata"
    # Kan teste på noke anna, men ser eg må sette meg litt meir inn i kordan det fungerer.


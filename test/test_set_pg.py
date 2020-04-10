import pytest
import set_pg

set_liste = ["Cheese", "Biscuit", "Sausage", "Wine", "Cheese", "Bread"]


def test_create_random_set():
    # Will return something random, will need to redesign test
    the_answer = {'Wine', 'Biscuit', 'Bread', 'Sausage', 'Cheese'}
    the_test = set_pg.create_random_set(set_liste)

    assert type(the_test) == type(the_answer), \
        f"Failed. Test: {the_test}, Answer: {the_answer}"


def test_create_random_list():
    # Will return something random, will need to redesign test
    the_test = set_pg.create_random_list(set_liste)
    the_answer = ['Cheese', 'Bread', 'Cheese', 'Bread', 'Bread', 'Bread', 'Biscuit', 'Bread', 'Wine', 'Sausage']
    assert type(the_test) == type(the_answer), \
        f"Failed. Test: {the_test}, answer: {the_answer}"

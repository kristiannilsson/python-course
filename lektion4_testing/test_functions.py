import pytest
from functions import add_numbers, subtract_numbers, divide_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(4, 7) == 11


def test_add_numbers2():
    assert add_numbers(6, 7) == 13


def test_subtract_numbers():
    assert subtract_numbers(11, 5) == 6


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5


def test_division_by_zero():
    with pytest.raises(SyntaxError):
        divide_numbers(10, 0)

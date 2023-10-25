import pytest #importerar pytest
from functions import add_numbers, subtract_numbers, divide_numbers #importerar ifrån functions


def test_add_numbers():
    assert add_numbers(2, 3) == 5 #assert är att du säkerställer att ett villkor är sant, är det falskt får du fel i testet.
    assert add_numbers(4, 7) == 11


def test_add_numbers2():
    assert add_numbers(6, 7) == 13


def test_subtract_numbers():
    assert subtract_numbers(11, 5) == 6


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError): #kollar att specifikt ZeroDivisionError kastas
        divide_numbers(10, 0)

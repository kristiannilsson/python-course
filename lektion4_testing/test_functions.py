from functions import add_numbers, divide_numbers
import pytest
def test_addition():
    assert add_numbers(2, 3) == 5


def test_division():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)
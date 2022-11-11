from example_2 import is_correct
from datetime import date
import pytest


@pytest.mark.parametrize("day, month, year, expected_result", [
    (31, 12, 2021, date(2021, 12, 31)),
    (20, 10, 2012, date(2012, 10, 20))
])
def test_is_correct(day, month, year, expected_result):
    assert is_correct(day, month, year) == expected_result


@pytest.mark.parametrize("day, month, year, expected_exception", [
    (33, 12, 2021, ValueError),
    (20, '10', 2012, TypeError)
])
def test_is_correct_with_error(day, month, year, expected_exception):
    with pytest.raises(expected_exception):
        is_correct(day, month, year)

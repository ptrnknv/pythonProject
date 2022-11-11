from example_2 import saturdays_between_two_dates
import pytest
from datetime import date

for i in range(1, 8):
    with open(f'../tests_3057804/{i}', 'r', encoding='utf-8') as file, open(f'../tests_3057804/{i}.clue') as answer:
        file.readline()
        file.readline()
        res = answer.readline()


@pytest.mark.parametrize("date1, date2, expected_result", [
    (date(date1), date(date2), res)
])
def test_saturdays_between_two_dates(date1, date2, expected_result):
    assert saturdays_between_two_dates(date1, date2) == expected_result


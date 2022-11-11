from example_2 import in_largest_units
import pytest


@pytest.mark.parametrize("param, expected_result", [(2343, '2 KB'),
                                                    (234434233, '224 MB')])
def test_in_largest_units(param, expected_result):
    assert in_largest_units(param) == expected_result


@pytest.mark.parametrize("expected_error, param", [(TypeError, '234523'),
                                                   (TypeError, [])])
def test_in_largest_units_with_error(expected_error, param):
    with pytest.raises(expected_error):
        assert in_largest_units(param)

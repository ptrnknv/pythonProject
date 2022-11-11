from example_2 import to_bytes
import pytest


@pytest.mark.parametrize("byte, unit, expected_result", [(1, 'KB', 1024),
                                                         (1, 'MB', 1024**2),
                                                         (1, 'GB', 1024**3),
                                                         (2, 'KB', 2048)
                                                         ])
def test_to_bytes_good(byte, unit, expected_result):
    assert to_bytes(byte, unit) == expected_result


@pytest.mark.parametrize("expected_exception, param", [(KeyError, 3),
                                                       (KeyError, "RB")])
def test_to_bytes_with_error(expected_exception, param):
    with pytest.raises(expected_exception):
        assert to_bytes(1, param) == 1024**3


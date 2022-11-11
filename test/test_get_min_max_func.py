import pytest

from example_2 import get_min_max
from datetime import *


def test_get_min_max():
    with pytest.raises(TypeError):
        assert get_min_max([date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]) == (datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))

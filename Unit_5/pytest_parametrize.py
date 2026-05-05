"""
Credit: https://edbennett.github.io/python-testing-ci/02-pytest-functionality/index.html
"""

import pytest

from arrays import add_arrays

@pytest.mark.parametrize("a, b, expect", [
    ([1, 2, 3],    [4, 5, 6],   [5, 7, 9]),
    ([-1, -5, -3], [-4, -3, 0], [-5, -8, -3]),
])
def test_add_arrays(a, b, expect):
    output = add_arrays(a, b)

    assert output == expect

def test_add_arrays_error():
    a = [1, 2, 3]
    b = [4, 5]
    with pytest.raises(ValueError):
        output = add_arrays(a, b)

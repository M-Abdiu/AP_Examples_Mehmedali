"""
Credit: https://edbennett.github.io/python-testing-ci/02-pytest-functionality/index.html
"""


import pytest

from arrays import add_arrays

@pytest.fixture
def pair_of_lists():
    return [1, 2, 3], [4, 5, 6]

def test_add_arrays(pair_of_lists):
    a, b = pair_of_lists
    expect = [5, 7, 9]

    output = add_arrays(a, b)

    assert output == expect
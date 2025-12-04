import pytest
from app import add, is_even


def test_add_simple():
    assert add(2, 3) == 5


def test_add_multiple():
    assert add(-1, 1) == 0
    assert add(10, 5) == 15


@pytest.mark.parametrize("value, expected", [
    (2, True),
    (3, False),
    (10, True),
    (11, False),
])
def test_is_even(value, expected):
    assert is_even(value) == expected


@pytest.fixture
def sample_numbers():
    return [2, 4, 6]


def test_all_even(sample_numbers):
    for n in sample_numbers:
        assert is_even(n)
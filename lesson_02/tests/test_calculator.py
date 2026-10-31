import pytest

from app.services.calculator import calculate_average, calculate_max, calculate_min
from app.utils.formatter import format_average


def test_average():
    assert calculate_average([5, 4, 5, 3, 5]) == pytest.approx(4.4)


def test_format():
    assert format_average(4.4) == "Средний результат: 4.40"


def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])


def test_min():
    assert calculate_min([5, 4, 5, 3, 5]) == 3


def test_min_empty():
    with pytest.raises(ValueError):
        calculate_min([])


def test_max():
    assert calculate_max([5, 4, 5, 3, 5]) == 5


def test_max_empty():
    with pytest.raises(ValueError):
        calculate_max([])

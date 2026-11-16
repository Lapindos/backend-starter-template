from pathlib import Path

import pytest

from app.services.calculator import (
    calculate_average,
    calculate_max,
    calculate_min,
    grade_bounds,
)
from app.services.report_file import save_report
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


def test_grade_bounds():
    assert grade_bounds([5, 4, 5, 3, 5]) == (3, 5)


def test_grade_bounds_empty():
    with pytest.raises(ValueError):
        grade_bounds([])


def test_save_report_new_file(tmp_path: Path):
    path = tmp_path / "report.txt"
    written = save_report(path, ["Средний результат: 4.40", "Минимальная оценка: 3"])
    assert written == 2
    assert path.read_text(encoding="utf-8") == (
        "Средний результат: 4.40\nМинимальная оценка: 3\n"
    )


def test_save_report_overwrites(tmp_path: Path):
    path = tmp_path / "report.txt"
    path.write_text("старый текст\n", encoding="utf-8")
    written = save_report(path, ["Максимальная оценка: 5"])
    assert written == 1
    assert path.read_text(encoding="utf-8") == "Максимальная оценка: 5\n"

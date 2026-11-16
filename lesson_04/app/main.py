"""Точка запуска Student Tools."""

from pathlib import Path

from rich.console import Console

from app.services.calculator import calculate_average, grade_bounds
from app.services.report_file import save_report
from app.utils.formatter import format_report

REPORT_PATH = Path("report.txt")


def main() -> None:
    """Считает оценки примера, печатает отчёт и записывает его в файл."""
    values = [5, 4, 5, 3, 5]
    average = calculate_average(values)
    low, high = grade_bounds(values)
    report = format_report(average, low, high)
    console = Console()
    console.print(report)
    save_report(REPORT_PATH, report.splitlines())


if __name__ == "__main__":
    main()

from rich.console import Console

from app.services.calculator import calculate_average, calculate_max, calculate_min
from app.utils.formatter import format_report


def main() -> None:
    values = [5, 4, 5, 3, 5]
    average = calculate_average(values)
    low = calculate_min(values)
    high = calculate_max(values)
    console = Console()
    console.print(format_report(average, low, high))


if __name__ == "__main__":
    main()

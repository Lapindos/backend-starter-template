def format_average(value: float) -> str:
    return f"Средний результат: {value:.2f}"


def format_min(value: int) -> str:
    return f"Минимальная оценка: {value}"


def format_max(value: int) -> str:
    return f"Максимальная оценка: {value}"


def format_report(average: float, low: int, high: int) -> str:
    return "\n".join(
        [
            format_average(average),
            format_min(low),
            format_max(high),
        ]
    )

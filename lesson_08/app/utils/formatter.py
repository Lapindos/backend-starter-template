"""Текст отчёта по оценкам. Числа сюда приходят уже посчитанными."""


def format_average(value: float) -> str:
    """Форматирует среднюю оценку с двумя знаками после точки.

    Args:
        value: Среднее в баллах.

    Returns:
        Строка со средней оценкой и двумя знаками после точки.
    """
    return f"Средний результат: {value:.2f}"


def format_min(value: int) -> str:
    """Форматирует минимальную оценку.

    Args:
        value: Наименьший балл.

    Returns:
        Строка с наименьшим баллом.
    """
    return f"Минимальная оценка: {value}"


def format_max(value: int) -> str:
    """Форматирует максимальную оценку.

    Args:
        value: Наибольший балл.

    Returns:
        Строка с наибольшим баллом.
    """
    return f"Максимальная оценка: {value}"


def format_report(average: float, low: int, high: int) -> str:
    """Собирает три строки отчёта в том порядке, в каком их печатают.

    Args:
        average: Средняя оценка в баллах.
        low: Минимальная оценка.
        high: Максимальная оценка.

    Returns:
        Три строки через перевод строки. Сначала среднее, затем минимум и максимум.
    """
    return "\n".join(
        [
            format_average(average),
            format_min(low),
            format_max(high),
        ]
    )

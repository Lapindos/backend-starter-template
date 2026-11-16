"""Текст отчёта по оценкам. Числа сюда приходят уже посчитанными."""


def format_average(value: float) -> str:
    """Форматирует среднюю оценку с двумя знаками после точки.

    Args:
        value: Среднее в баллах.

    Returns:
        Строка вида «Средний результат: 4.40».
    """
    return f"Средний результат: {value:.2f}"


def format_min(value: int) -> str:
    """Форматирует минимальную оценку.

    Args:
        value: Наименьший балл.

    Returns:
        Строка вида «Минимальная оценка: 3».
    """
    return f"Минимальная оценка: {value}"


def format_max(value: int) -> str:
    """Форматирует максимальную оценку.

    Args:
        value: Наибольший балл.

    Returns:
        Строка вида «Максимальная оценка: 5».
    """
    return f"Максимальная оценка: {value}"


def format_report(average: float, low: int, high: int) -> str:
    """Собирает три строки отчёта в том порядке, в каком их печатают.

    Args:
        average: Средняя оценка в баллах.
        low: Минимальная оценка.
        high: Максимальная оценка.

    Returns:
        Три строки через перевод строки: среднее, минимум, максимум.
    """
    return "\n".join(
        [
            format_average(average),
            format_min(low),
            format_max(high),
        ]
    )

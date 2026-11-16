"""Расчёты по списку целочисленных оценок."""


def calculate_average(values: list[int]) -> float:
    """Считает среднее арифметическое оценок.

    Args:
        values: Оценки целыми баллами. Пустой список не принимается.

    Returns:
        Среднее. Деление без округления, единица измерения — балл.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return sum(values) / len(values)


def calculate_min(values: list[int]) -> int:
    """Возвращает наименьшую оценку.

    Args:
        values: Оценки целыми баллами. Пустой список не принимается.

    Returns:
        Наименьший балл из списка.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return min(values)


def calculate_max(values: list[int]) -> int:
    """Возвращает наибольшую оценку.

    Args:
        values: Оценки целыми баллами. Пустой список не принимается.

    Returns:
        Наибольший балл из списка.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return max(values)


def grade_bounds(values: list[int]) -> tuple[int, int]:
    """Возвращает границы оценок: сначала минимум, затем максимум.

    Args:
        values: Оценки целыми баллами. Пустой список не принимается.

    Returns:
        Пара баллов. Первый элемент — минимум, второй — максимум.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return min(values), max(values)

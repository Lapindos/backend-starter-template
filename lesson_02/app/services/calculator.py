def calculate_average(values: list[int]) -> float:
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return sum(values) / len(values)


def calculate_min(values: list[int]) -> int:
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return min(values)


def calculate_max(values: list[int]) -> int:
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return max(values)

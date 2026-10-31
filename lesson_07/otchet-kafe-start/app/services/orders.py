"""Заказы смены: чтение файла, выручка по официантам и сортировка."""

from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    """Читает заказы из CSV и собирает список Order.

    Args:
        path: Путь к файлу смены, в строках есть официант и сумма в копейках.

    Returns:
        Список заказов в том порядке, в каком строки лежат в файле.
    """
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Считает выручку каждого официанта и отдаёт её по убыванию суммы.

    Args:
        orders: Заказы смены. Пустой список не считается.
        top: Сколько официантов оставить, начиная с самой большой выручки.
            Ноль означает всех.

    Returns:
        Словарь «имя официанта — сумма в копейках».

    Raises:
        ValueError: Если список заказов пуст.
    """
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    """Сортирует заказы по сумме в копейках, от большей к меньшей.

    Args:
        orders: Список, который функция меняет на месте. Новый список не создаётся.
    """
    orders.sort(key=lambda order: -order.kopeks)

from rich.table import Table


def format_report(count, total, average, expensive_day, expensive_sum, food_share, housing_share):
    table = Table(title="ОТЧЁТ ПО ПОЕЗДКЕ")
    table.add_column("Показатель")
    table.add_column("Значение", justify="right")
    table.add_row("записей", str(count))
    table.add_row("всего потрачено", f"{total} ₽")
    table.add_row("средняя трата", f"{average:.2f} ₽")
    table.add_row("самый дорогой день", f"день {expensive_day}, {expensive_sum} ₽")
    table.add_row("доля категории «еда»", f"{food_share:.2f} %")
    table.add_row("доля категории «жильё»", f"{housing_share:.2f} %")
    return table

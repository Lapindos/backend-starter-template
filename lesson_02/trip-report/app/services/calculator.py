def calculate_total(expenses):
    if not expenses:
        return 0
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    return calculate_total(expenses) / len(expenses)


def most_expensive_day(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    by_day = {}
    for expense in expenses:
        day = expense["day"]
        by_day[day] = by_day.get(day, 0) + expense["amount"]
    day = max(by_day, key=by_day.get)
    return day, by_day[day]


def category_share(expenses, category):
    if not expenses:
        raise ValueError("список расходов пуст")
    spent = 0
    found = False
    for expense in expenses:
        if expense["category"] == category:
            spent += expense["amount"]
            found = True
    if not found:
        raise ValueError("такой категории нет")
    return spent / calculate_total(expenses) * 100

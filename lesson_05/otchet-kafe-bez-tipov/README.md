# Отчёт кафе — аннотации расставлены

Исходный проект был без аннотаций. У параметров, результатов и методов
проставлены типы. Поля `Order` аннотациями уже были: для dataclass это
объявление поля.

## Запуск

    python3 -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python main.py

Отчёт печатается так же, как в проекте с аннотациями: Python их при запуске
не проверяет.

## Проверки

    python -m pytest -v              # 12 тестов
    mypy app                         # Success: no issues found in 15 source files

## Что оставлено как есть

Поля заказа в app/domain/order.py записаны с аннотациями: это dataclass,
и для него аннотация — объявление поля. Без неё поля не будет.

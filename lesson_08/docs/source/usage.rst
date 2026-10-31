Запуск и проверки
=================

Как запустить
-------------

Команды выполняются из папки ``lesson_08``.

Что печатает программа:

- среднюю оценку;
- минимальную оценку;
- максимальную оценку.

.. code-block:: text

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python -m app.main

Запись файла делает :func:`app.services.report_file.save_report`.
Границы оценок считает :func:`app.services.calculator.grade_bounds`.

Проверки
--------

.. code-block:: text

   python -m pytest -v
   mypy app
   ruff check app

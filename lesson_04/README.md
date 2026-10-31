# Student Tools

**Студент:** Марущак Сергей, группа РПО 25/2

Программа считает среднюю, минимальную и максимальную оценку, печатает отчёт
через Rich и записывает его в `report.txt`.

**Python:** 3.12.3

Путь интерпретатора из активированного `.venv`:

```text
/agent/repos/backend-starter-template/lesson_04/.venv/bin/python
```

Команда: `python -c "import sys; print(sys.executable)"`.

## Структура

```
lesson_04/
├── app/__init__.py                 пакет
├── app/main.py                     запуск, печать и запись отчёта
├── app/services/calculator.py      среднее, минимум, максимум, границы
├── app/services/report_file.py     запись отчёта в файл
├── app/utils/formatter.py          строки отчёта
├── tests/test_calculator.py
├── docs/help.txt                   вывод help() по двум модулям
├── pyproject.toml                  mypy и Ruff
├── .vscode/settings.json           формат Google и режим basic
├── requirements.txt
├── .gitignore
└── README.md
```

`calculator.py` только считает. На пустом списке функции вызывают `ValueError`.
`formatter.py` только собирает текст. `report_file.py` только пишет файл и
перезаписывает его, если он уже есть. `main.py` соединяет части.

Рецензия практикума «Младший разработчик» лежит рядом:
`podpisi_Марущак_Сергей.md`.

## Команды

Linux и macOS, из папки `lesson_04`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
python -m pytest -v
mypy app
ruff check app
```

Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
python -m pytest -v
mypy app
ruff check app
```

## Ожидаемый результат

```text
Средний результат: 4.40
Минимальная оценка: 3
Максимальная оценка: 5
```

Тесты: `11 passed`. Файл `report.txt` создаётся при запуске и в репозиторий
не входит.

## Формат докстрингов

Формат Google. Типы из аннотаций в тексте докстринга не повторяются.
В `pyproject.toml` у Ruff конвенция `google`, у mypy включён
`disallow_untyped_defs`. В `.vscode/settings.json` формат генератора
`google`, режим проверки типов `basic`.

## Проверка

```text
python -m pytest -v
11 passed

mypy app
Success: no issues found in 7 source files

ruff check app
All checks passed!
```

Поиск строк `_summary_` и `_description_` по пакету `app` ничего не находит.
`docs/help.txt` читается подряд: сначала модуль `calculator`, затем
`report_file`.

## Почему `.venv` не кладут в репозиторий

Окружение собирается заново на каждом компьютере. Внутри бинарные файлы
одной системы и абсолютные пути. В Git передаётся `requirements.txt`.

## Проверка на чистом месте

Папка скопирована без `.venv`. Новое окружение собрано из `requirements.txt`.
Запуск, pytest, mypy и ruff прошли с тем же выводом.

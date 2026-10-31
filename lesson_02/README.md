# Student Tools

**Студент:** Марущак Сергей, группа РПО 25/2

Программа считает среднюю, минимальную и максимальную оценку и печатает отчёт через Rich.

**Python:** 3.12.3

Путь интерпретатора из активированного `.venv`:

```text
/agent/repos/backend-starter-template/lesson_02/.venv/bin/python
```

Команда: `python -c "import sys; print(sys.executable)"`.

## Структура

```
lesson_02/
├── app/__init__.py
├── app/main.py                   оценки примера, вызовы расчётов, печать
├── app/services/calculator.py    среднее, минимум и максимум
├── app/utils/formatter.py        строки отчёта, без расчётов
├── tests/test_calculator.py      семь тестов
├── requirements.txt
├── .gitignore
└── README.md
```

`calculator.py` только считает и на пустом списке вызывает `ValueError`.
`formatter.py` только собирает текст. `main.py` соединяет части.

## Команды

Linux и macOS, из папки `lesson_02`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
python -m pytest -v
```

Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
python -m pytest -v
```

## Ожидаемый результат

```text
Средний результат: 4.40
Минимальная оценка: 3
Максимальная оценка: 5
```

Тесты: `7 passed`. Три исходных проверки среднего и формата и четыре новых:
минимум и максимум на обычном списке и на пустом.

## Почему `.venv` не кладут в репозиторий

Окружение собирается заново на каждом компьютере. Внутри бинарные файлы
одной системы и абсолютные пути. Чужой компьютер из чужой `.venv` проект
не запустит. В Git передаётся `requirements.txt`, по нему окружение
создаётся командами выше.

## Проверка на чистом месте

Папка скопирована без `.venv`. Новое окружение собрано через
`pip install -r requirements.txt`. `python -m pytest -q` прошёл,
`python -m app.main` напечатал 4.40, 3 и 5.

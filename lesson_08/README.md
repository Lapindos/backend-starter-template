# Student Tools

**Студент:** Марущак Сергей, группа РПО 25/2

Программа считает среднюю, минимальную и максимальную оценку, печатает отчёт
через Rich и записывает его в `report.txt`.

**Python:** 3.12.3

Путь интерпретатора из активированного `.venv`:

```text
/agent/repos/backend-starter-template/lesson_08/.venv/bin/python
```

## Структура

```
lesson_08/
├── app/                  расчёты, запись файла, оформление, запуск
├── tests/                11 тестов
├── docs/source/          исходники сайта Sphinx
├── docs/requirements.txt Sphinx 9.1.1 и Furo 2025.12.19
├── pyproject.toml        mypy и Ruff
├── requirements.txt
└── README.md
```

`calculator.py` только считает. На пустом списке функции вызывают `ValueError`.
`report_file.py` перезаписывает существующий файл. `formatter.py` только
собирает текст.

## Команды

Linux и macOS, из папки `lesson_08`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r docs/requirements.txt
python -m app.main
python -m pytest -v
mypy app
ruff check app
sphinx-build -M html docs/source docs/build -E -W --keep-going
```

Страницы пакетов заново:

```bash
SPHINX_APIDOC_OPTIONS=members sphinx-apidoc -f -M -o docs/source/api app
```

## Ожидаемый результат

```text
Средний результат: 4.40
Минимальная оценка: 3
Максимальная оценка: 5
```

Тесты: `11 passed`. `mypy app` — `Success: no issues found in 7 source files`.
`ruff check app` — `All checks passed!`.

## Формат докстрингов

Формат Google. Типы из аннотаций в тексте не повторяются.
В первой строке раздела `Returns` нет двоеточия: иначе Napoleon принимает
кусок фразы за тип результата.

## Документация

Сборка локально:

```bash
sphinx-build -M html docs/source docs/build -E -W --keep-going
```

Страницы пакетов пересоздаются командой `sphinx-apidoc` из раздела «Команды».
Сайт публикуется workflow `.github/workflows/docs.yml` при изменениях в
`lesson_08`.

Адрес сайта: будет вписан после первого зелёного запуска Actions.

## Почему `.venv` не кладут в репозиторий

Окружение и `docs/build/` собираются заново. В Git их нет.

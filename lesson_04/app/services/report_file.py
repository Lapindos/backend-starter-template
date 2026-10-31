"""Запись готового отчёта в текстовый файл."""

from pathlib import Path


def save_report(path: Path, lines: list[str]) -> int:
    """Записывает строки отчёта в файл UTF-8.

    Args:
        path: Куда записать отчёт. Существующий файл перезаписывается целиком.
        lines: Строки отчёта без перевода строки на конце каждой строки.

    Returns:
        Число записанных строк.
    """
    text = "\n".join(lines)
    if lines:
        text += "\n"
    path.write_text(text, encoding="utf-8")
    return len(lines)

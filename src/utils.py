import json
from typing import Any


def convert_transactions(path_json: str) -> list[dict[str, Any]]:
    """Функция, которая возвращает список словарей данных транзакций из JSON-файла"""
    try:
        with open(path_json, encoding="utf-8") as file:
            transactions: list[dict[str, Any]] = json.load(file)
        return transactions
    except Exception:
        return []


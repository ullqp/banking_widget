import json
from typing import Any

from logger.logger import utils_logger


def convert_transactions(path_json: str) -> list[dict[str, Any]]:
    """Функция, которая возвращает список словарей данных транзакций из JSON-файла"""
    try:
        utils_logger.info("Открытие файла, возвращение данных.")
        with open(path_json, encoding="utf-8") as file:
            transactions: list[dict[str, Any]] = json.load(file)
        return transactions
    except Exception as ex:
        utils_logger.error(f"Произошла ошибка: {ex}")
    return []

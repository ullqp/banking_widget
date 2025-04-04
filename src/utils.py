import json
from typing import Any

import pandas as pd

from logger.logger import utils_logger


def read_json(path_json: str) -> list[dict[str, Any]]:
    """Функция, которая возвращает список словарей данных транзакций из JSON-файла"""
    try:
        utils_logger.info("Открытие файла, возвращение данных.")
        with open(path_json, encoding="utf-8") as file:
            transactions: list[dict[str, Any]] = json.load(file)
        return transactions
    except Exception as ex:
        utils_logger.error(f"Произошла ошибка: {ex}")
    return []


def read_csv(path_to_file: str) -> list | str:
    """Функция, которая считывает транзакции из CSV-файла."""
    try:
        transactions_list = pd.read_csv(path_to_file, sep=";", engine="python", encoding="utf-8")
        result = transactions_list.to_dict(orient="records")
        print(result)
        return result
    except Exception as e:
        return f"Ошибка: {e}"


def read_excel(path_to_file: str) -> list:
    """Функция, которая считывает транзакции из EXCEL-файла."""
    transactions_list = pd.read_excel(path_to_file)
    return transactions_list.to_dict(orient="records")

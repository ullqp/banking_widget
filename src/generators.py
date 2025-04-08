from typing import Iterator


def filter_by_currency(transactions: list, currency: str, file_type: int) -> Iterator[dict]:
    """
    Функция, которая сортирует операции по валюте.
    Для file_type: .json = 1, .csv = 2, .xlsx = 3.
    """
    if file_type == 1:
        currency_transactions = list(
            filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
        )
    elif file_type in [2, 3]:
        currency_transactions = list(filter(lambda x: x["currency_code"] == currency, transactions))
    if currency_transactions == []:
        yield {}

    for transaction in currency_transactions:
        yield transaction


def filter_rub_transactions(transactions: list[dict], file_type: str) -> list[dict] | None:
    """
    Фильтрует транзакции по валюте RUB (если only_rub=True).
    Работает с вложенной структурой currency.
    Для file_type: .json = 1, .csv = 2, .xlsx = 3.
    """
    if file_type == "1":
        return [
            txn
            for txn in transactions
            if txn.get("operationAmount", {}).get("currency", {}).get("code") in ("RUB", "RUR")
            or "руб" in str(txn.get("operationAmount", {}).get("currency", {}).get("name", "")).lower()
        ]
    elif file_type in ["2", "3"]:
        return [
            txn
            for txn in transactions
            if txn.get("currency_code", {}) in ("RUB", "RUR") or "руб" in str(txn.get("currency_name", {})).lower()
        ]


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """Функция, которая возвращает описания транзакций."""
    descriptions = list(map(lambda x: x["description"], transactions))
    if descriptions == []:
        yield ""

    for description in descriptions:
        yield description


def card_number_generator(start: int, finish: int) -> Iterator[str]:
    """Функция, которая генерирует номера банковских карт."""
    x = start
    if finish > 9999999999999999:
        finish = 9999999999999999
    while x <= finish:
        number = str(x).zfill(16)
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
        x += 1

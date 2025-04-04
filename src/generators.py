from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """Функция, которая сортирует операции по валюте."""
    currency_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    if currency_transactions == []:
        yield {}

    for transaction in currency_transactions:
        yield transaction


def filter_rub_transactions(transactions: list[dict], only_rub: bool) -> list[dict]:
    """
    Фильтрует транзакции по валюте RUB (если only_rub=True).
    Работает с вложенной структурой currency.
    """
    if not only_rub:
        return transactions

    return [
        txn
        for txn in transactions
        if txn.get("operationAmount", {}).get("currency", {}).get("code") in ("RUB", "RUR")
        or "руб" in str(txn.get("operationAmount", {}).get("currency", {}).get("name", "")).lower()
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

import re
from collections import Counter


def find_description(transactions_list: list[dict], marker: str) -> list[dict]:
    """Фильтрует транзакции по наличию подстроки в поле description."""
    found_transactions: list[dict] = []
    pattern = re.compile(marker, flags=re.IGNORECASE)

    for transaction in transactions_list:
        description = transaction.get("description")
        if not isinstance(description, str):
            continue

        if re.search(pattern, description):
            found_transactions.append(transaction)

    return found_transactions


def count_categories(transactions_list: list[dict], marker_categories: list) -> dict:
    """Подсчитывает количество транзакций по категориям на основе описания."""
    counted_categories = {}
    counted = Counter([transaction["description"].lower() for transaction in transactions_list])
    for marker_category in marker_categories:
        pattern = re.compile(marker_category.lower())
        for value, count in counted.items():
            if pattern.search(value.lower()):
                counted_categories[marker_category] = count

    return counted_categories

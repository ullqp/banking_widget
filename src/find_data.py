# Напишите функцию, которая будет принимать список словарей с данными о
# банковских операциях и список категорий операций, а возвращать словарь,
# в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
# Категории операций хранятся в поле
# description

import re
from collections import Counter


def find_description(transactions_list: list[dict], marker: str) -> list[dict]:
    found_transactions: list[dict] = []
    pattern = re.compile(marker, flags=re.IGNORECASE)

    for transaction in transactions_list:
        if transaction.get("description") is None:
            transactions_list.remove(transaction)
            continue
        i = re.search(pattern, transaction["description"])
        if i:
            found_transactions.append(transaction)

    return found_transactions



def count_categories(transactions_list: list[dict], marker_categories: list) -> dict[str: int]:
    counted_categories = {}
    counted = Counter([transaction["description"].lower() for transaction in transactions_list])
    for marker_category in marker_categories:
        pattern = re.compile(marker_category.lower())
        for value, count in counted.items():
            if pattern.search(value.lower()):
                counted_categories[marker_category]=count

    return counted_categories

# transactions = [
#         {
#             "id": 441945886,
#             "state": "EXECUTED",
#             "date": "2019-08-26T10:50:58.294041",
#             "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод организации",
#             "from": "Maestro 1596837868705199",
#             "to": "Счет 64686473678894779589",
#         },
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
# "description": "ПОЛУЧЕНИе организации",
#             "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#         },
# ]
#
# # # print(find_description(transactions, 'перевод'))
# print(count_categories(transactions, ['Перевод организации', 'ПОлучение организации']))
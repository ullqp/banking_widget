from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Пример использования mask_account_card
card = "Visa Platinum 7000792289606361"
mask_account_card(card)

# Пример использования get_date
date = "2024-03-11T02:26:18.671407"
get_date(date)

# Пример использования filter_by_state
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 59402872, "state": "CANCELLED", "date": "2018-09-17T21:27:25.241241"},
]
filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)

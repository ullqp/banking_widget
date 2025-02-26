# Проект "Banking widget"

## Описание:

Проект "Banking widget" - это серверная часть виджета банковских операций, с возможностью отображать операции клиента.

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/ullqp/banking_widget.git
```

## Использование:

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

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

# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

# Пример использования transaction_descriptions
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
    
# Пример использования card_number_generator
for card_number in card_number_generator(1, 5):
    print(card_number)

```

### Тестирование

Для тестирования проекта используется библиотека `pytest`. Чтобы запустить тесты, выполните команду:

```bash
pytest
```

Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `mask_account_card` и `get_data`.
- `processing`: функции `filter_by_state` и `sort_by_date`.
- `generators`: функции `filter_by_currency`, `transaction_descriptions` и `card_number_generator`

Покрытие тестами составляет более 80% кода проекта.

---
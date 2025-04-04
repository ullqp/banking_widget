import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency(transactions: list) -> None:
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 939719574,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency2(transactions: list) -> None:
    generator = filter_by_currency(transactions, "REWREWF")
    assert next(generator) == {}


def test_filter_by_currency3() -> None:
    generator = filter_by_currency([], "RUB")
    assert next(generator) == {}


def test_transaction_descriptions(transactions: list) -> None:
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions2() -> None:
    generator = transaction_descriptions([])
    assert next(generator) == ""


@pytest.mark.parametrize(
    "start, finish, expected_result",
    [
        (1, 2, "0000 0000 0000 0001"),
        (99999, 100000, "0000 0000 0009 9999"),
        (123456789, 123456790, "0000 0001 2345 6789"),
        (9999999999999999, 10000000000000000, "9999 9999 9999 9999"),
        (9999999999999998, 9999999999999999, "9999 9999 9999 9998"),
    ],
)
def test_card_number_generator(start: int, finish: int, expected_result: str) -> None:
    generator = card_number_generator(start, finish)
    assert next(generator) == expected_result

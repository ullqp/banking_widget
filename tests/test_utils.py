from typing import Any
from unittest.mock import patch

from src.utils import read_java


@patch("json.load")
@patch("builtins.open")
def test_convert_transactions(mock_open: Any, mock_load: Any) -> None:
    mock_load.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        },
    ]

    mock_open.return_value.__enter__.return_value = None

    result = read_java("test.json")

    assert result == mock_load.return_value
    mock_open.assert_called_once_with("test.json", encoding="utf-8")
    mock_load.assert_called_once()


@patch("json.load")
@patch("builtins.open")
def test_convert_transactions2(mock_open: Any, mock_load: Any) -> None:
    mock_load.return_value = []

    mock_open.return_value.__enter__.return_value = None

    result = read_java("test.json")

    assert result == mock_load.return_value
    mock_open.assert_called_once_with("test.json", encoding="utf-8")
    mock_load.assert_called_once()

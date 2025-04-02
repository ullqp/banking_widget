from typing import Any
from unittest.mock import patch

from src.external_api import transaction_amount


@patch("requests.request")
def test_transaction_amount(mock_get: Any) -> None:

    mock_get.return_value.json.return_value = {"result": 841.9}

    result = transaction_amount({"operationAmount": {"amount": "10", "currency": {"name": "USD", "code": "USD"}}})

    assert result == 841.9

    mock_get.assert_called_once()
    call_args = mock_get.call_args[0]
    assert call_args[0] == "GET"
    assert call_args[1] == "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10.0"


@patch("requests.request")
def test_transaction_amount_rub(mock_get: Any) -> None:

    result = transaction_amount({"operationAmount": {"amount": "1000", "currency": {"name": "RUB", "code": "RUB"}}})

    assert result == 1000.0

    mock_get.assert_not_called()

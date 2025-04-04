import unittest
from typing import Any
from unittest.mock import patch

import pandas as pd

from src.utils import read_csv, read_excel, read_json


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

    result = read_json("test.json")

    assert result == mock_load.return_value
    mock_open.assert_called_once_with("test.json", encoding="utf-8")
    mock_load.assert_called_once()


@patch("json.load")
@patch("builtins.open")
def test_convert_transactions2(mock_open: Any, mock_load: Any) -> None:
    mock_load.return_value = []

    mock_open.return_value.__enter__.return_value = None

    result = read_json("test.json")

    assert result == mock_load.return_value
    mock_open.assert_called_once_with("test.json", encoding="utf-8")
    mock_load.assert_called_once()


class TestReadCSV(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_read_csv(self, mock_read_csv: Any) -> None:
        """Тестирование функции, читающий CSV-файл."""
        # Настройка mock объекта для возврата DataFrame
        mock_read_csv.return_value = pd.DataFrame(
            [
                {
                    "id": "650703",
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": "16210",
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                }
            ]
        )

        path_to_file: str = "transactions.csv"

        result: list[dict] | str = read_csv(path_to_file)

        expected_result: list[dict] = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()


class TestReadEXCEL(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_excel(self, mock_read_excel: Any) -> None:
        """Тестирование функции, читающий EXCEL-файл."""
        # Настройка mock объекта для возврата DataFrame
        mock_read_excel.return_value = pd.DataFrame(
            [
                {
                    "id": "650703",
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": "16210",
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                }
            ]
        )

        path_to_file = "transactions_excel.xlsx"

        result = read_excel(path_to_file)

        expected_result = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

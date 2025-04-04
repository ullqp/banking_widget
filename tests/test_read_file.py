import unittest
from typing import Any
from unittest.mock import patch

import pandas as pd

from src.read_file import read_csv, read_excel


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

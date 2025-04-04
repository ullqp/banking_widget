import re
import unittest


def find_description(transactions: list[dict], marker: str) -> list[dict]:
    pattern = re.compile(marker, flags=re.IGNORECASE)
    return [t for t in transactions if isinstance(t.get("description"), str) and pattern.search(t["description"])]


def count_categories(transactions: list[dict], markers: list[str]) -> dict[str, int]:
    descriptions = [t["description"].lower() for t in transactions if isinstance(t.get("description"), str)]
    return {marker: sum(1 for desc in descriptions if re.search(marker.lower(), desc)) for marker in markers}


class TestBankTransactions(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {
                "id": 441945886,
                "description": "Перевод организации",
                "operationAmount": {"currency": {"code": "RUB", "name": "руб."}},
            },
            {
                "id": 41428829,
                "description": "Перевод организации",
                "operationAmount": {"currency": {"code": "USD", "name": "USD"}},
            },
            {
                "id": 939719570,
                "description": "Открытие вклада",
                "operationAmount": {"currency": {"code": "RUB", "name": "руб."}},
            },
            {"id": 587085106, "description": None, "operationAmount": {"currency": {"code": "RUB", "name": "руб."}}},
        ]

    def test_find_description(self) -> None:
        # Поиск по части описания
        result = find_description(self.transactions, "перевод")
        self.assertEqual(len(result), 2)
        self.assertEqual({t["id"] for t in result}, {441945886, 41428829})

        # Регистронезависимый поиск
        result = find_description(self.transactions, "ОТКРЫТИЕ")
        self.assertEqual(result[0]["id"], 939719570)

        # Нет совпадений
        self.assertEqual(len(find_description(self.transactions, "платеж")), 0)

    def test_count_categories(self) -> None:
        # Подсчет категорий
        result = count_categories(self.transactions, ["перевод", "вклад"])
        self.assertEqual(result, {"перевод": 2, "вклад": 1})

        # Пустые результаты
        self.assertEqual(count_categories(self.transactions, ["кредит"]), {"кредит": 0})


if __name__ == "__main__":
    unittest.main()

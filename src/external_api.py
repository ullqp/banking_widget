import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}

def transaction_amount(transaction: dict) -> float | str:
    """Функция, которая возвращает сумму транзакции в рублях."""
    amount: float = float(transaction["operationAmount"]["amount"])
    from_currency: str = transaction["operationAmount"]["currency"]["code"]
    if from_currency == "RUB":
        return amount
    else:

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"
        response = requests.request("GET", url, headers=headers)
        answer = response.json()
        return float(answer["result"])



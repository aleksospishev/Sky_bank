import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = "https://api.apilayer.com/exchangerates_data/convert"
headers = {"apikey": API_KEY}


def conversion_currency_amount(code_currency: str, amount: float, code_currency_out: str = "RUB") -> dict:
    """Функция обращается к API с суммой транзакции и кодом валюты возвращает JSON с конвертированной суммой."""
    params = {"to": code_currency_out, "from": code_currency, "amount": amount}
    return requests.get(URL, headers=headers, params=params).json()

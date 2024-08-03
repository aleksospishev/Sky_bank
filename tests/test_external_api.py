import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv

from src.external_api import conversion_currency_amount

load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = "https://api.apilayer.com/exchangerates_data/convert"
HEADERS = {"apikey": API_KEY}
PARAMS = {"to": "RUB", "from": "EUR", "amount": 3.5}


def test_conversion_currency_amount_response() -> None:
    """функцция проверяет, что с верными атрибутами запроса, сервер отвечает кодом 200"""
    response = requests.get(URL, headers=HEADERS, params=PARAMS)
    assert response.status_code == 200


def test_conversion_currency_amount_response_bad_request() -> None:
    """функцция проверяет, что с неверными атрибутами запроса, сервер отвечает кодом 400"""
    response = requests.get(URL, headers=HEADERS)
    assert response.status_code == 400


@patch("requests.get")
def test_conversion_currency_amount(mock_get) -> None:
    """проверяет корректность работы функции обращения к api"""
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 3.5},
        "info": {"timestamp": 1722687916, "rate": 93.288055},
        "date": "2024-08-03",
        "result": 326.508193,
    }
    assert conversion_currency_amount("EUR", 3.5) == {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 3.5},
        "info": {"timestamp": 1722687916, "rate": 93.288055},
        "date": "2024-08-03",
        "result": 326.508193,
    }
    mock_get.assert_called_once_with(URL, headers=HEADERS, params=PARAMS)

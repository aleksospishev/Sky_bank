import csv
from unittest.mock import Mock, patch

import pandas

from src.read_file import csv_or_xls_read_file

data_test = [
    {
        "id": 4137938,
        "state": "EXECUTED",
        "date": "2023-01-04T13:13:34Z",
        "amount": 15560,
        "currency_name": "Real",
        "currency_code": "BRL",
        "from": "",
        "to": "Счет 38164279390569873521",
        "description": "Открытие вклада",
    },
    {
        "id": 4699552,
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "amount": 23423,
        "currency_name": "Peso",
        "currency_code": "PHP",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
        "description": "Перевод с карты на карту",
    },
]


def test_read_file_csv():
    assert csv_or_xls_read_file("./data_test/test.csv") == data_test


def test_read_file_xls():
    assert csv_or_xls_read_file("./data_test/test.xlsx") == data_test


def test_read_file_not_csv():
    assert csv_or_xls_read_file("./data_test/test.json") == []


def test_not_file():
    assert csv_or_xls_read_file("not_file.csv") == "файл не найден введите корректный путь"

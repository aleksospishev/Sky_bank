from src.read_file import csv_or_xls_read_file
import pandas as pd
from unittest.mock import patch
import pytest

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


@pytest.fixture
def test_df() -> pd.DataFrame:
    return pd.DataFrame(data_test)


@patch('src.read_file.pd.read_csv')
def test_read_file_csv(mock_read, test_df):
    """Тест чтение из файла CSV."""
    mock_read.return_value = test_df
    res = csv_or_xls_read_file("./data_test/test.csv")
    expected = test_df.to_dict(orient='records')
    assert res == expected


@patch('src.read_file.pd.read_excel')
def test_read_file_csv(mock_read, test_df):
    """Тест чтение из файла xls."""
    mock_read.return_value = test_df
    res = csv_or_xls_read_file("./data_test/test.xlsx")
    expected = test_df.to_dict(orient='records')
    assert res == expected
    mock_read.assert_called_once_with("./data_test/test.xlsx")


def test_read_file_not_csv():
    """Тест чтение из файла Не CSV & XLS."""
    assert csv_or_xls_read_file("./data_test/test.json") == []


def test_not_file():
    """Тест чтение из несуществующего файла."""
    assert csv_or_xls_read_file("not_file.csv") == "файл не найден введите корректный путь"

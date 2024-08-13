import pytest

from src.utis import amount_transaction_return, inlet_json_file


def test_inlet_json_file() -> None:
    """Тест функции считывания JSON на корректном файле."""
    res = inlet_json_file("./data_test/test.json")
    assert res == [{"hello": "world"}, {"Hi": "friend"}]


def test_inlet_json_file_not_file() -> None:
    """Тест функции считывания JSON на отсутвующем файле."""
    res = inlet_json_file("./data_test/not_file.json")
    assert res == []


def test_inlet_json_file_not_data() -> None:
    """Тест функции считывания JSON на пустом файле."""
    res = inlet_json_file("./data_test/not_data.json")
    assert res == []


@pytest.fixture
def data_test_rub() -> dict:
    """Фикстура для тестов."""
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "10", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def data_test_eur() -> dict:
    """Фикстура для тестов."""
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "3.5", "currency": {"name": "руб.", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_amount_transaction_return_rub(data_test_rub: dict) -> None:
    """Тест где валюта рубляю."""
    assert amount_transaction_return(data_test_rub) == 10

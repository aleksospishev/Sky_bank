import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def date_test() -> str:
    """Фикстура даты для тестов."""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def date_test_2() -> str:
    """Фикстура даты_2 для тестов."""
    return "2024-07-12 21:03:21.725047"


def test_get_date() -> None:
    """Тест трансформации даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-07-12 21:03:21.725047") == "12.07.2024"
    assert get_date("12.07.2024") == "Некорректные данные"
    assert get_date("") == "Некорректные данные"


def test_mask_account_card() -> None:
    """Тест маскирования карты аккаунта."""
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("Счет 447895560") == "Счет **5560"
    assert mask_account_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert mask_account_card("") == "Некорректные данные"
    assert mask_account_card("Мир 64686473678894779589") == "Некорректные данные"

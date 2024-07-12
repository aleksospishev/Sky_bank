import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "my_num, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (0, "0"),
        ("1234567812345678", "Некорректные данные"),
        ("Hello", "Некорректные данные"),
        (None, "Некорректные данные"),
    ],
)
def test_get_mask_card_number(my_num, expected):
    assert get_mask_card_number(my_num) == expected


@pytest.mark.parametrize(
    "my_num, expected",
    [
        (73654108430135874305, "**4305"),
        ("1234567812345678", "Некорректные данные"),
        (1234, "Некорректные данные"),
        ("Hello world", "Некорректные данные"),
        (None, "Некорректные данные"),
    ],
)
def test_get_mask_account(my_num, expected):
    assert get_mask_account(my_num) == expected

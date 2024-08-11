from typing import Generator


def filter_by_currency(transactions: list[dict], сurrency: str) -> Generator:
    """Генератор который фильтрует записи из всех банковских операцийпо признаку - код валюты."""
    filter_transactions = (el for el in transactions if el["operationAmount"]["currency"]["code"] == сurrency)
    for el in filter_transactions:
        yield el


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Генератор который выдает описание каждой операции."""
    descriptions_transaction = (el["description"] for el in transactions)
    for el in descriptions_transaction:
        yield el


def card_number_generator(start: int, end: int) -> Generator:
    """Генератор который генерирует номер карты в формате ХХХХ ХХХХ ХХХХ ХХХХ с номером из диапозона."""
    while start <= end:
        mask = "0" * (16 - len(str(start))) + str(start)
        mask_card = mask[:4] + " " + mask[4:8] + " " + mask[8:12] + " " + mask[12:]
        yield mask_card
        start += 1

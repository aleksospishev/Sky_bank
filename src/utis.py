import json

from src.external_api import conversion_currency_amount


def inlet_json_file(file_name):
    """Функция принимает путь до файла и возвращает возвращает список словарей"""
    try:
        with open(file_name) as file:
            data_json = json.load(file)
    except FileNotFoundError:
        data_json = []
    except json.JSONDecodeError:
        data_json = []
    return data_json


def amount_transaction_return(transaction: dict) -> float:
    """"Принимает транзакцию и возвращает сумму покупки в формате Float если валюта транзакции отлична от RUB
    происходит конвертация через api по средствам функции 'conversion_currency_amount'"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        amount_currency = transaction["operationAmount"]["currency"]["code"]
        amount_transaction = transaction["operationAmount"]["amount"]
        conversion_json = conversion_currency_amount(amount_currency, amount_transaction)
        return round(conversion_json["result"], 2)

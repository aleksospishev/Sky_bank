import json
import logging

from src.external_api import conversion_currency_amount

utils_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def inlet_json_file(file_name: str) -> list:
    """Функция принимает путь до файла и возвращает возвращает список словарей."""
    try:
        utils_logger.info(f"Считываем данные из файла {file_name} ")
        with open(file_name) as file:
            data_json = json.load(file)
            utils_logger.info("данные успешно считаны")
    except FileNotFoundError:
        data_json = []
        utils_logger.warning("Отсутвует файл JSON")
    except json.JSONDecodeError:
        utils_logger.warning("Файл JSON пустой")
        data_json = []
    return data_json


def amount_transaction_return(transaction: dict):
    """Функция трансформации суммы в валюте.

    Принимает транзакцию и возвращает сумму покупки в формате Float если валюта транзакции отлична от RUB
    происходит конвертация через api по средствам функции 'conversion_currency_amount'.
    """
    utils_logger.info(f'Обрабатываем транзакцию id {transaction["id"]}')
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        res = float(transaction["operationAmount"]["amount"])
    else:
        amount_currency = transaction["operationAmount"]["currency"]["code"]
        amount_transaction = float(transaction["operationAmount"]["amount"])
        conversion_json = conversion_currency_amount(amount_currency, amount_transaction)
        utils_logger.info(f"Обращаемся к API для конвертации {amount_currency} {amount_transaction}")
        res = round(conversion_json["result"], 2)
    return res

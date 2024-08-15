import logging

from src.generators import filter_by_currency
from src.processing import filter_by_state, search_operations_by_description, sort_by_date
from src.read_file import csv_or_xls_read_file
from src.utils import inlet_json_file
from src.widget import get_date, mask_account_card

GREETINGS_TEXT = """Привет! Добро пожаловать в программу работы с банковскими транзакциями.

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""

main_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/main.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
main_logger.addHandler(file_handler)
main_logger.setLevel(logging.DEBUG)

answer_files = {
    1: ["JSON", "./data/operations.json"],
    2: ["CSV", "./data/transactions.csv"],
    3: ["xlsx", "./data/transactions_excel.xlsx"],
}


def handler_file(file_type: str, file_path) -> None:
    """Функция выбора какой функцией обрабатывать файл"""
    if file_type == "JSON":
        return inlet_json_file(file_path)
    elif file_type == "CSV" or file_type == "xlsx":
        return csv_or_xls_read_file(file_path)


def main():
    """MAIN функция проекта."""
    answer = input(GREETINGS_TEXT)
    try:
        main_logger.info(f"Пользователь ввел {answer}")
        type_file = answer_files.get(int(answer))[0]
        path_file = answer_files.get(int(answer))[1]
        print(f"Для обработки выбран {type_file}-файл")
        main_logger.info(f"Считываем данные из файла {path_file}")
        data = handler_file(type_file, path_file)
    except TypeError as e:
        main_logger.error(f"{e} пользователь выбрал неподдерживаемый тип файла")
        print("Вы выбрали неподдерживаемый формат файла.")
    # print(data)
    data_sort = None
    while data_sort is None:
        answer_status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        if answer_status.upper() in ("EXECUTED", "CANCELED", "PENDING"):
            main_logger.info(f"Пользователь ввел {answer_status} ")
            data_sort = filter_by_state(data, answer_status.upper())
        main_logger.warning(f"Пользователь ввел {answer_status}")
    main_logger.info("Требуется ли сортировка данных по дате?")
    answer_sort_date = input("Отсортировать операции по дате? Да/Нет\n")
    main_logger.info(f"Пользователь ввел {answer_sort_date} ")
    if answer_sort_date.lower() == "да":
        main_logger.info(f"Вызываем {sort_by_date}")
        answer_descending = input("Отсортировать по возрастанию или по убыванию?\n")
        descending = True
        if answer_descending.lower() == "по возрастанию":
            descending = False
        data_sort = sort_by_date(data_sort, descending)
    main_logger.info("Требуется ли сортировка по валюте транзакции")
    answer_sort_currency = input("Выводить только рублевые тразакции? Да/Нет\n")
    if answer_sort_currency.lower() == "да":
        data_sort = list(filter_by_currency(data_sort, "RUB"))
    answer_sort_descriptions = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    main_logger.info(f"пользователь ввел {answer_sort_descriptions}")
    if answer_sort_descriptions.lower() == "да":
        word_descriptions = input("Введите ключевое для поиска слово\n")
        data_sort = search_operations_by_description(data_sort, word_descriptions.lower())
    print("Распечатываю итоговый список транзакций...")
    if len(data_sort) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data_sort)}\n")
        for el in data_sort:
            date = get_date(el["date"])
            if el["description"] == "Открытие вклада":
                transaction_from_to = mask_account_card(el["to"])
            else:
                from_trans, to_trans = mask_account_card(el["from"]), mask_account_card(el["to"])
                transaction_from_to = f"{from_trans} -> {to_trans}"

            print(
                f"""{date} {el['description']}
{transaction_from_to}
Сумма: {round(float(el["operationAmount"]["amount"]))} {el["operationAmount"]["currency"]["code"]}
"""
            )


if __name__ == "__main__":
    main()

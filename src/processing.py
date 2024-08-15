import re
from collections import Counter, defaultdict


def filter_by_state(list_dictionary: list, state_meaning: str = "EXECUTED") -> list:
    """Фильтр State.

    Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению.
    """
    result = []
    for elem in list_dictionary:
        if state_meaning == elem.get("state"):
            result.append(elem)
    return result


def sort_by_date(list_dictionary: list, descending: bool = True) -> list:
    """Сортировка по дате транзакции.

    Принимает список словарей и необязательный параметр, задающий порядок сортировки, возвращать новый список,
    отсортированный по дате.
    """
    return sorted(list_dictionary, key=lambda list_dictionary: list_dictionary.get("date"), reverse=descending)


def search_operations_by_description(list_operations: list[dict], str_description: str) -> list:
    """Поиск по описанию.

    Принимает спикок словарей с данными об операциях и строку поиска, возвращает те операции где в описании есть строка
    поиска.
    """
    result = []
    for el in list_operations:
        if re.search(str_description, el.get("description", "").lower()):
            result.append(el)
    return result


def count_operations_by_description(list_operations: list[dict], list_descriptions: list) -> dict:
    """Подсчет количества операций по описанию

    Функция принимает список банковских операций и список описаний, вывоит словарь в котором ключ это описание, а
    значение количество транзакций с таким описанием
    """
    counted = Counter([el.get("description") for el in list_operations])
    res = defaultdict(int)
    for elem in list_descriptions:
        res[elem] = counted[elem]
    return res

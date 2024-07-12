def filter_by_state(list_dictionary: list, state_meaning: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению."""
    result = []
    for elem in list_dictionary:
        if state_meaning == elem.get("state"):
            result.append(elem)
    return result


def sort_by_date(list_dictionary: list, descending: bool = True) -> list:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки, возвращать новый список,
    отсортированный по дате."""

    return sorted(list_dictionary, key=lambda list_dictionary: list_dictionary.get("date"), reverse=descending)

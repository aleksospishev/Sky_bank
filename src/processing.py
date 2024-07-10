def filter_by_state(list_dictionary: list[dict], state_meaning: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению."""
    result = []
    for elem in list_dictionary:
        if state_meaning == elem.get("state"):
            result.append(elem)
    return result


def sort_by_date(list_dictionary: list[dict], ascending: bool = False) -> list[dict]:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки, возвращать новый список,
    отсортированный по дате."""
    return sorted(list_dictionary, key=lambda list_dictionary: list_dictionary["date"], reverse=not ascending)

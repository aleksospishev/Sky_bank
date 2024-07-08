from .masks import get_mask_account, get_mask_card_number
# import masks

TYPE_CARDS = ["visa", "mastercard", "maestro"]


def mask_account_card(input_string: str) -> str:
    """Принимает строку в которой указан номер и тип карты или номер счета,
    возвращает замаскированную строку"""
    list_input = input_string.split()
    if list_input[0].lower() in TYPE_CARDS:

        return f"{' '.join(list_input[:-1])} {get_mask_card_number(list_input[-1])}"
    elif list_input[0].lower() == "счет":
        return f"{' '.join(list_input[:-1])} {get_mask_account(list_input[-1])}"
    else:
        return "Введены некоректные данные"


def get_date(date_input: str) -> str:
    temp = date_input[0:10].split('-')
    return f'{temp[2]}.{temp[1]}.{temp[0]}'


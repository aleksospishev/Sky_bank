from .masks import get_mask_account, get_mask_card_number

# import masks

TYPE_CARDS = ["visa", "mastercard", "maestro"]


def mask_account_card(input_string: str) -> str:
    """Принимает строку в которой указан номер и тип карты или номер счета,возвращает замаскированную строку."""
    list_input = input_string.split()
    if list_input[0].lower() in TYPE_CARDS:
        message = f"{' '.join(list_input[:-1])} {get_mask_card_number(int(list_input[-1]))}"
    elif list_input[0].lower() == "счет":
        message = f"{' '.join(list_input[:-1])} {get_mask_account(int(list_input[-1]))}"
    else:
        message = "Введены некоректные данные"
    return message


def get_date(date_input: str) -> str:
    """Принимает дату в формату 'YYYY-MM-DDTHH:MM:SS.ms' возвращает в формате 'DD.MM.YYYY'."""
    temp = date_input[0:10].split("-")
    return f"{temp[2]}.{temp[1]}.{temp[0]}"

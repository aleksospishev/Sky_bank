def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты в формате 'XXXX XX** **** XXXX'."""
    if type(card_number) is int:
        number_card = str(card_number)
        mask_card_number = ""
        for i in range(1, len(number_card) + 1):
            if i <= 6 or i > len(number_card) - 4:
                mask_card_number += number_card[i - 1]
            else:
                mask_card_number += "*"
            if (i % 4) == 0 and i != len(number_card):
                mask_card_number += " "
        return mask_card_number
    else:
        return "Некорректные данные"


def get_mask_account(account: int) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    if type(account) is int:
        if len(str(account)) > 6:
            return "**" + str(account)[-4:]
        else:
            return "Некорректные данные"
    else:
        return "Некорректные данные"

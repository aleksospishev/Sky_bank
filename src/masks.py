def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты в формате 'XXXX XX** **** XXXX'."""
    number_card = str(card_number)
    mask_card_number = ""
    for i in range(1, len(number_card) + 1):
        if i <= 6 or i > len(number_card) - 4:
            mask_card_number += number_card[i - 1]
        else:
            mask_card_number += "*"
        if (i % 4) == 0:
            mask_card_number += " "
    return mask_card_number


def get_mask_account(account: int) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    return "**" + str(account)[-4:]

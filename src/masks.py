import logging

masks_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты в формате 'XXXX XX** **** XXXX'."""
    if type(card_number) is int:
        masks_logger.info(f"трансформируем карту с номером {card_number} ")
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
        masks_logger.warning(f"{card_number} -некорректные данные")
        return "Некорректные данные"


def get_mask_account(account: int) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    if type(account) is int:
        if len(str(account)) > 6:
            masks_logger.info(f"трансформируем аккаунт {account}")
            return "**" + str(account)[-4:]
        else:
            masks_logger.warning(f"{account} -некорректные данные")
            return "Некорректные данные"
    else:
        masks_logger.warning(f"{account} -некорректные данные")
        return "Некорректные данные"

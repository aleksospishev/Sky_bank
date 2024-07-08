import datetime
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date


def main():
    """Необязаь=тельный тест функций."""
    # string = input()
    # print(mask_account_card(string))
    date = datetime.datetime.now()
    print(date)
    print(get_date(str(date)))


if __name__ == "__main__":
    main()

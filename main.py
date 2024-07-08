from src.masks import get_mask_account, get_mask_card_number


def main():
    """Необязаь=тельный тест функций."""
    card_number = int(input())
    account = int(input())
    print(get_mask_card_number(card_number))
    print(get_mask_account(account))


if __name__ == "__main__":
    main()

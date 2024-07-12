from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card
from src.masks import get_mask_card_number, get_mask_account


def main() -> None:
    # """Для чего то что то."""
    # test = input()
    # print(mask_account_card(test))
    # test_list = [
    #     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    # ]
    # print(filter_by_state(test_list, "CANCELED"))
    # print(sort_by_date(test_list))
    #
    # print(get_mask_card_number(7000792289606361) == '7000 79** **** 6361')
    #
    # print (get_mask_card_number(''))
    # num = int(input())
    # print(get_mask_card_number(num))

    # print(get_mask_account(1234))
    data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            # {'id': 414258829},
            {'id': 93979570, 'date': '2018-06-30T02:08:58.425572'},
            # {'id': 414829, 'state': 'EXECUTED'},
            ]
    print(sort_by_date(data))
    print(type(filter_by_state(data)))


if __name__ == "__main__":
    main()

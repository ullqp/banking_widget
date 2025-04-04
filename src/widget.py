from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или счёта."""
    if not isinstance(account_card, str):
        return ''
    elif "Счет" in account_card:
        return f"Счет {get_mask_account(account_card[5:])}"
    else:
        type_card: str = ""
        for i in account_card:
            if i not in "0123456789":
                type_card += i
        return f"{type_card}{get_mask_card_number(account_card[len(type_card):])}"



def get_date(start_date: str) -> str:
    """Функция, которая преобразует дату."""
    if (
        start_date[4] == start_date[7] == "-"
        and start_date[10] == "T"
        and start_date[13] == start_date[16] == ":"
        and start_date[19] == "."
    ):
        numbers: str = (
            start_date[:4]
            + start_date[5:7]
            + start_date[8:10]
            + start_date[11:13]
            + start_date[14:16]
            + start_date[17:19]
            + start_date[20:]
        )
        if numbers.isdigit():
            return f"{start_date[8:10]}.{start_date[5:7]}.{start_date[:4]}"
        else:
            return "Некорректная дата."
    else:
        return "Некорректная дата."

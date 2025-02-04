from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или счёта."""
    if "Счет" in account_card:
        return f"Счет **{get_mask_account(account_card[-4:])}"
    else:
        type_card: str = ""
        for i in account_card:
            if i not in "0123456789":
                type_card += i
        return f"{type_card}{get_mask_card_number(account_card[len(type_card):])}"


def get_date(start_date: str) -> str:
    """Функция, которая преобразует дату."""
    return f"{start_date[8:10]}.{start_date[5:7]}.{start_date[:4]}"

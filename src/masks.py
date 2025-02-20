def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты."""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Некорректный номер карты."


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счёта."""
    if len(account_number) > 5 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Некорректный номер счёта."

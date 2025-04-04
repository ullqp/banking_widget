from datetime import datetime

from src.masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или счёта."""
    if not isinstance(account_card, str):
        return "Некорректный номер карты."

    account_card = account_card.strip()
    if not account_card:
        return "Некорректный номер карты."

    if "Счет" in account_card:
        # Для счетов - принимаем любую длину (даже 1 цифру)
        account_number = account_card[5:].strip()
        if not account_number.isdigit():
            return "Счет Некорректный номер счёта."
        # Всегда маскируем последние 4 цифры (или меньше, если номер короче)
        return f"Счет **{account_number[-4:] if len(account_number) >= 4 else account_number}"
    else:
        # Для карт - минимум 12 цифр
        parts = account_card.split()
        if len(parts) < 2:
            return "Некорректный номер карты."

        card_name = " ".join(parts[:-1])
        card_number = parts[-1]

        if not card_number.isdigit() or len(card_number) < 12:
            return "Некорректный номер карты."

        return f"{card_name} {get_mask_card_number(card_number)}"


def get_date(start_date: str) -> str:
    """Преобразует дату из формата ISO 8601 (например, 2020-11-28T00:38:44Z) в DD.MM.YYYY."""
    if not isinstance(start_date, str):
        return "Некорректная дата."

    try:
        if "Z" in start_date:
            start_date = start_date.replace("Z", "+00:00")
        dt = datetime.fromisoformat(start_date)
        return dt.strftime("%d.%m.%Y")
    except (ValueError, AttributeError):
        return "Некорректная дата."

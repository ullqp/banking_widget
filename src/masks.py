from logger.logger import masks_logger


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты."""
    try:
        masks_logger.info("Маскируем номер карты")
        if len(card_number) == 16 and card_number.isdigit():
            return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    except Exception as ex:
        masks_logger.error(f"Произошла ошибка: {ex}")
    return "Некорректный номер карты."


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счёта."""
    try:
        masks_logger.info("Маскируем номер счёта")
        if len(account_number) > 5 and account_number.isdigit():
            return f"**{account_number[-4:]}"
    except Exception as ex:
        masks_logger.error(f"Произошла ошибка: {ex}")
    return "Некорректный номер счёта."

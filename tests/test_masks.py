from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(number: str) -> None:
    """
    Тестирует функцию маскировки номера карты.
    Проверяет работу с корректными значениями.
    """
    assert get_mask_card_number(number) == "7000 79** **** 6361"


def test_get_mask_account(number: str) -> None:
    """
    Тестирует функцию маскировки номера счета.
    Проверяет работу с корректными значениями.
    """

    assert get_mask_account(number) == "**6361"

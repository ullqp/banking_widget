from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    """
    Тестирует функцию маскировки карты и счета.
    Проверяет работу с корректными и некорректными значениями.
    """
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("MasterCaard 7158300734726758") == "Неккоректное имя карты или счёта."


def test_get_date() -> None:
    """
    Тестирует функцию преобразования даты.
    Проверяет работу с корректными и некорректными значениями.
    """
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-05-01T21:00:00.671407") == "01.05.2024"
    assert get_date("2024-05-g1T21:00:00.671407") == "Некорректная дата."

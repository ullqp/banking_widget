from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    """Тестирует функцию маскировки карты и счета."""
    # Тесты для карт
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

    # Тесты для счетов
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 123") == "Счет **123"  # Короткий номер
    assert mask_account_card("Счет 12") == "Счет **12"  # Очень короткий номер
    assert mask_account_card("Счет 1") == "Счет **1"  # Минимальный номер

    # Краевые случаи
    assert mask_account_card("") == "Некорректный номер карты."
    assert mask_account_card("Счет") == "Счет Некорректный номер счёта."
    assert mask_account_card("Счет abc") == "Счет Некорректный номер счёта."
    assert mask_account_card("Карта") == "Некорректный номер карты."
    assert mask_account_card(123) == "Некорректный номер карты."  # type: ignore
    assert mask_account_card(None) == "Некорректный номер карты."  # type: ignore


def test_get_date() -> None:
    """Тестирует функцию преобразования даты."""
    # Корректные даты
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-05-01T21:00:00.671407") == "01.05.2024"
    assert get_date("2020-11-28T00:38:44Z") == "28.11.2020"
    assert get_date("2023-07-15T12:30:45+03:00") == "15.07.2023"

    # Некорректные даты
    assert get_date("2024-05-g1T21:00:00.671407") == "Некорректная дата."
    assert get_date("не дата") == "Некорректная дата."
    assert get_date("") == "Некорректная дата."
    assert get_date(None) == "Некорректная дата."  # type: ignore
    assert get_date(123456) == "Некорректная дата."  # type: ignore

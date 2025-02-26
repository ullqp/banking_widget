import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(number: str) -> None:
    """
    Тестирует функцию маскировки номера карты.
    Проверяет работу с корректными значениями.
    """
    assert get_mask_card_number(number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "numbers, expected_result",
    [
        ("700079228960636171", "Некорректный номер карты."),
        ("qwertyuiogeg6361", "Некорректный номер карты."),
        ("12345", "Некорректный номер карты."),
    ],
)
def test_get_mask_card_number2(numbers: str, expected_result: str) -> None:
    """
    Тестирует функцию маскировки номера карты.
    Проверяет работу с некорректными вводами.
    """
    assert get_mask_card_number(numbers) == expected_result


def test_get_mask_account(number: str) -> None:
    """
    Тестирует функцию маскировки номера счета.
    Проверяет работу с корректными значениями.
    """

    assert get_mask_account(number) == "**6361"


@pytest.mark.parametrize(
    "numbers, expected_result",
    [
        ("874305", "**4305"),
        ("32423d324", "Некорректный номер счёта."),
        ("3453", "Некорректный номер счёта."),
    ],
)
def test_mask_account(numbers: str, expected_result: str) -> None:
    """
    Тестирует функцию маскировки номера счета.
    Проверяет работу с пограничным значением и некорректными вводами.
    """
    assert get_mask_account(numbers) == expected_result

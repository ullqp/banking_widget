import pytest

from src.masks import get_mask_account, get_mask_card_number


# Фикстура для тестирований функций максировки счета и номера карты
@pytest.fixture
def number() -> str:
    return "7000792289606361"


@pytest.mark.parametrize(
    "numbers, expected_result",
    [
        ("700079228960636171", "Некорректный номер карты."),
        ("qwertyuiogeg6361", "Некорректный номер карты."),
        ("12345", "Некорректный номер карты."),
    ],
)
def test_get_mask_card_number(numbers: str, expected_result: str) -> None:
    """
    Тестирует функцию маскировки номера карты.
    Проверяет работу с некорректными вводами.
    """
    assert get_mask_card_number(numbers) == expected_result


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


# Фикстура для тестирований функций фильтрации по состоянию и сортировки по дате
@pytest.fixture
def operations1() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстура для тестирований функций фильтрации по состоянию и сортировки по дате
@pytest.fixture
def operations2() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "201845310-1T408:2о:33.419441"},
    ]

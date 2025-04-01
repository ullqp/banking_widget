import pytest

from src.decorators import log


@log()
def my_function(x: int, y: int) -> int:
    """Функция для проверки декоратора, которая нацело делит на 2 сумму переданных чисел."""
    return (x + y) // 2


def test_log(capsys: pytest.CaptureFixture) -> None:

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log2(capsys: pytest.CaptureFixture) -> None:

    my_function(1, "2")
    captured = capsys.readouterr()
    assert (
        captured.out == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"
    )


def test_log3(capsys: pytest.CaptureFixture) -> None:
    filename = "mylog.txt"

    @log(filename=filename)
    def my_function(x: int, y: int) -> int:
        """Функция для проверки декоратора, которая складывает два переданных числа."""
        return x + y

    my_function(1, 2)
    with open(f"logs/{filename}", "r") as text:
        line = text.readline()
    assert line == "my_function ok\n"


def test_log5(capsys: pytest.CaptureFixture) -> None:
    filename = "log.txt"

    @log(filename=filename)
    def my_function(x: int, y: int) -> int:
        """Функция для проверки декоратора, которая складывает два переданных числа."""
        return x + y

    my_function(1, "cat")
    with open(f"logs/{filename}", "r") as text:
        line = text.readline()
    assert line == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'cat'), {}\n"

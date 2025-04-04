from pathlib import Path

from _pytest.capture import CaptureFixture

from src.decorators import log

LOGS_DIR = Path(__file__).parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True, parents=True)


def clear_log_file(filename: str) -> None:
    """Очищает файл лога если он существует"""
    log_path = LOGS_DIR / filename
    if log_path.exists():
        log_path.unlink()


@log()
def divide_sum(x: int, y: int) -> int:
    """Делит сумму чисел на 2"""
    return (x + y) // 2


@log(filename="test_log.txt")
def add_numbers(x: int, y: int) -> int:
    """Складывает два числа"""
    return x + y


def test_log_stdout_success(capsys: CaptureFixture[str]) -> None:
    """Проверка вывода в stdout при успешном выполнении"""
    result: int = divide_sum(4, 6)
    captured = capsys.readouterr()
    assert result == 5
    assert captured.out == "divide_sum ok\n"


def test_log_stdout_error(capsys: CaptureFixture[str]) -> None:
    """Проверка вывода в stdout при ошибке"""
    result: Optional[int] = divide_sum(4, "6")  # type: ignore
    captured = capsys.readouterr()
    assert result is None
    assert "unsupported operand type" in captured.out


def test_log_file_success() -> None:
    """Проверка записи в файл при успешном выполнении"""
    clear_log_file("test_log.txt")
    result: int = add_numbers(3, 5)

    log_path: Path = LOGS_DIR / "test_log.txt"
    assert log_path.exists(), f"Файл {log_path} не был создан"
    assert result == 8
    assert "add_numbers ok" in log_path.read_text()


def test_log_file_error() -> None:
    """Проверка записи в файл при ошибке"""
    clear_log_file("test_log.txt")
    result: Optional[int] = add_numbers(3, "5")  # type: ignore

    log_path: Path = LOGS_DIR / "test_log.txt"
    assert log_path.exists(), f"Файл {log_path} не был создан"
    assert result is None
    assert "add_numbers error" in log_path.read_text()


def test_log_preserves_metadata() -> None:
    """Проверка сохранения метаданных функции"""
    assert divide_sum.__name__ == "divide_sum"
    assert divide_sum.__doc__ is not None
    assert "делит сумму" in divide_sum.__doc__.lower()

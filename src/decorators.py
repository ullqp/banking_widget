import typing
from functools import wraps

from logs import current_directory

# from time import time

# from logs import current_directory


def log(filename: str | None = None) -> typing.Callable:
    """Параметр для декоратора, который отвечает за названия файла, куда сохраняется лог."""

    def decorator(func: typing.Callable) -> typing.Callable:
        """Декоратор, который логирует переданную функцию."""

        def save_log(log_message: str) -> None:
            """Функция, которая выводит или сохраняет в файл лог."""
            if filename is None:
                return print(log_message)

            with open(f"{current_directory}\\{filename}", "a") as f:
                f.write(log_message + "\n")

        @wraps(func)
        def wrapper(*args: typing.Any, **kwargs: dict) -> None:
            """Функция, которая фиксирует работу функции."""
            # start = time()
            # end = None
            log_message = None

            try:
                result = func(*args, **kwargs)
                # end = time()
                log_message = f"{func.__name__} ok"
            except Exception as e:
                # end = time()
                log_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

            return save_log(log_message)

        return wrapper

    return decorator


filename = "ba.txt"


@log(filename=filename)
def my_function(x: int, y: int) -> int:
    """Функция для проверки декоратора, которая складывает два переданных числа."""
    return x + y


my_function(1, 2)

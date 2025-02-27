from functools import wraps
from typing import Any, Callable

from logs import current_directory

# from time import time



def log(filename: str | None = None) -> Callable:
    """Параметр для декоратора, который отвечает за названия файла, куда сохраняется лог."""

    def decorator(func: Callable) -> Callable:
        """Декоратор, который логирует переданную функцию."""

        def save_log(log_message: str) -> None:
            """Функция, которая выводит или сохраняет в файл лог."""
            if filename is None:
                return print(log_message)

            with open(f"{current_directory}\\{filename}", "a") as f:
                f.write(log_message + "\n")

        @wraps(func)
        def wrapper(*args: Any, **kwargs: dict) -> Any:
            """Функция, которая фиксирует работу функции."""
            # start = time()
            # end = None
            log_message: str
            result: int|None = None
            try:
                result = func(*args, **kwargs)
                # end = time()
                log_message = f"{func.__name__} ok"
            except Exception as e:
                # end = time()
                log_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
            save_log(log_message)
            return result

        return wrapper

    return decorator

import pandas as pd


def read_csv(path_to_file: str) -> list | str:
    """Функция, которая считывает транзакции из CSV-файла."""
    try:
        transactions_list = pd.read_csv(path_to_file)
        return transactions_list.to_dict(orient="records")
    except Exception as e:
        return f"Ошибка: {e}"


def read_excel(path_to_file: str) -> list:
    """Функция, которая считывает транзакции из EXCEL-файла."""
    transactions_list = pd.read_excel(path_to_file)
    return transactions_list.to_dict(orient="records")

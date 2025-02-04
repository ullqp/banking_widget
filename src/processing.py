def filter_by_state(operations_list: list, state: str = "EXECUTED") -> list:
    """Функция, которая фильтрует данные о банковских операциях."""
    new_list: list = list()
    for i in operations_list:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def sort_by_date(operations_list: list, reverse: str = "True") -> list:
    """Функция, которая сортирует операции по дате."""
    new_list: list = sorted(
        operations_list,
        key=lambda x: x["date"][:4]
        + x["date"][5:7]
        + x["date"][8:10]
        + x["date"][11:13]
        + x["date"][14:16]
        + x["date"][17:19],
        reverse=reverse == "True",
    )
    return new_list

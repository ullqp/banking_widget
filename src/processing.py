def filter_by_state(operations_list: list, state: str = "EXECUTED") -> list:
    """Функция, которая фильтрует данные о банковских операциях."""
    new_list: list = list()
    for operation in operations_list:
        if "state" in operation.keys():
            if operation["state"] == state:
                new_list.append(operation)
        else:
            new_list.append(operation)
    return new_list


def sort_by_date(operations_list: list, reverse: bool = True) -> list:
    """Функция, которая сортирует операции по дате."""
    for operation in operations_list:
        numbers: str = (
            operation["date"][:4]
            + operation["date"][5:7]
            + operation["date"][8:10]
            + operation["date"][11:13]
            + operation["date"][14:16]
            + operation["date"][17:19]
        )
        if not numbers.isdigit():
            operations_list.remove(operation)
            print(operations_list)

    new_list: list = sorted(
        operations_list,
        key=lambda operation: operation["date"][:4]
        + operation["date"][5:7]
        + operation["date"][8:10]
        + operation["date"][11:13]
        + operation["date"][14:16]
        + operation["date"][17:19],
        reverse=reverse == True,
    )
    return new_list

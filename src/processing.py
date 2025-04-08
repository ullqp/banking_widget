from datetime import datetime


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


def sort_by_date(operations_list: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список операций по дате (по убыванию по умолчанию)."""

    def parse_date(date_value: str) -> datetime:
        """Парсит дату из строки, числа или None, учитывая разные форматы."""
        if date_value is None:
            raise ValueError("Дата отсутствует")

        # Если дата уже в формате datetime
        if isinstance(date_value, datetime):
            return date_value

        # Если дата - число (timestamp или подобное)
        if isinstance(date_value, (int, float)):
            try:
                return datetime.fromtimestamp(date_value)
            except (ValueError, OSError):
                raise ValueError("Некорректный timestamp")

        # Если дата - строка
        if isinstance(date_value, str):
            if date_value.endswith("Z"):
                date_value = date_value.replace("Z", "+00:00")
            try:
                return datetime.fromisoformat(date_value)
            except ValueError:
                raise ValueError("Некорректный формат даты")

        raise ValueError("Неподдерживаемый тип даты")

    filtered_operations = []
    for operation in operations_list:
        date_value = operation.get("date")
        try:
            operation["_parsed_date"] = parse_date(date_value)
            filtered_operations.append(operation)
        except ValueError:
            continue

    sorted_operations = sorted(
        filtered_operations,
        key=lambda op: op["_parsed_date"],
        reverse=reverse,
    )

    for op in sorted_operations:
        op.pop("_parsed_date", None)

    return sorted_operations

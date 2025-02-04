def filter_by_state(list_dictionary: list, state: str='EXECUTED') -> list:
    """Функция, которая фильтрует данные о банковских операциях."""
    new_dictionary: list = list()
    for i in list_dictionary:
        if i['state'] == state:
            new_dictionary.append(i)
    return new_dictionary


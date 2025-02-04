def filter_by_state(list_dictionary: list, state: str='EXECUTED') -> list:
    """Функция, которая фильтрует данные о банковских операциях."""
    new_dictionary: list = list()
    for i in list_dictionary:
        if i['state'] == state:
            new_dictionary.append(i)
    return new_dictionary


def sort_by_date(list_dictionary: list, reverse: str='True') -> list:
    """Функция, которая сортирует операции по дате."""
    new_dictionary: list = sorted(list_dictionary, key=lambda x: x['date'][:4]+x['date'][5:7]+x['date'][8:10]
                                                           +x['date'][11:13]+x['date'][14:16]+x['date'][17:19],
                                  reverse=reverse=='True')
    return new_dictionary
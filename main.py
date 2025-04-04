from src.find_data import find_description
from src.generators import filter_by_currency, filter_rub_transactions
from src.processing import filter_by_state, sort_by_date
from src.utils import read_csv, read_excel, read_json
from src.widget import get_date, mask_account_card

path_to_java = "../banking_widget-hw_13_2/data/operations.json"
path_to_csv = "../banking_widget-hw_13_2/data/transactions.csv"
path_to_xlsx = "../banking_widget-hw_13_2/data/transactions.xlsx"


success = False

menu = {"1": "JSON", "2": "CSV", "3": "XLSX"}


print(
    """Привет! Добро пожаловать в программу работы
с банковскими транзакциями. """
)
selected_menu = ""

while not success:
    user_answer = input(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

"""
    )
    try:
        print(f"\nДля обработки выбран {menu[user_answer]}-файл.\n")
        selected_menu = user_answer
        success = True

    except Exception:
        print("\nВведите корректное значение!\n")

file_to_open = selected_menu
if selected_menu == "1":
    operations = read_json(path_to_java)
elif selected_menu == "2":
    operations = read_csv(path_to_csv)
elif selected_menu == "3":
    operations = read_excel(path_to_xlsx)


statuses = ["executed", "canceled", "pending"]
success = False

selected_status = ""

while not success:

    user_answer = input(
        """\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\n"""
    )
    if user_answer.lower() in statuses:
        print(f"\nОперации отфильтрованы по статусу {user_answer.upper()}\n")
        selected_status = user_answer
        success = True
    else:
        print(f"\nСтатус операции {user_answer} недоступен.\n")


filtered_transactions = filter_by_state(operations, state=selected_status.upper())


selected_sorted = {"sort_date": "", "reverse": "", "only_rub": "", "word_marker": ""}
answer_yes_no = {
    "да": True,
    "нет": False,
}
other_answer = {"по возрастанию": True, "по убыванию": False}


success = False
while not success:
    answer_sort_date = input("\nОтсортировать операции по дате? Да/Нет\n\n").lower()
    if answer_sort_date in answer_yes_no:
        selected_sorted["sort_date"] = answer_yes_no[answer_sort_date]
        success = True
    else:
        print("\nВведите корректное значение!\n")


if selected_sorted["sort_date"]:
    success = False
    while not success:
        answer_reverse = input("\nОтсортировать по возрастанию или по убыванию?\n\n").lower()
        if answer_reverse in other_answer:
            selected_sorted["reverse"] = other_answer[answer_reverse]
            success = True

            operations_list = sort_by_date(operations, reverse=selected_sorted["reverse"])
        else:
            print("\nВведите корректное значение!\n")

success = False
while not success:
    answer_rub = input("\nВыводить только рублевые транзакции? Да/Нет\n\n").lower()
    if answer_rub in answer_yes_no:
        selected_sorted["only_rub"] = answer_yes_no[answer_rub]

        operations = filter_rub_transactions(operations, only_rub=selected_sorted["only_rub"])
        success = True
    else:
        print("\nВведите корректное значение!\n")

success = False
while not success:
    answer_word = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n\n").lower()
    if answer_word in answer_yes_no:
        if answer_word == "да":
            selected_sorted["word_marker"] = input("\nВведите слово:\n")
        success = True
    else:
        print("\nВведите корректное значение!\n")


print("\nРаспечатываю итоговый список транзакций...\n")

try:
    if selected_sorted["sort_date"]:
        operations = sort_by_date(operations, reverse=selected_sorted["sort_date"])

    if selected_sorted["only_rub"]:
        operations = list(filter_by_currency(operations, "RUB"))

    if selected_sorted["word_marker"] != "":
        operations = find_description(operations, selected_sorted["word_marker"])

except Exception:
    print("\nВозникла ошибка, попробуйте еще раз.\n")

count_operations = len(operations)
if count_operations > 0:
    print(f"\nВсего банковских операций в выборке: {count_operations}\n")

    for operation in operations:

        date = operation.get("date", "")
        if date != "" and isinstance(date, str):
            date = get_date(date)

        description = operation.get("description", "")

        print(date, description)

        number2 = operation.get("to", "")
        if number2 != "" and isinstance(number2, str):
            number2 = mask_account_card(number2)

        number1 = operation.get("from", "")
        if number1 != "" and isinstance(number1, str):
            number1 = mask_account_card(number1)

            print(f"{number1} -> {number2}")
        else:
            print(number2)

        amount = ""
        currency = ""
        if file_to_open == "1":
            operationAmount = operation.get("operationAmount")
            amount = ""
            currency = ""
            if operationAmount:
                amount = operationAmount.get("amount", "")
                currency = operationAmount.get("currency", "")
                if currency != "":
                    currency = currency.get("name")
        elif file_to_open == "2" or file_to_open == "3":
            amount = operation.get("amount", "")
            currency = operation.get("currency_name", "")
        print(f"Сумма: {amount} {currency}\n")

else:
    print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации\n")


"""
2
canceled
да
по возрастанию
нет
да
перевод

"""

from src.csv_xlsx_read import read_transactions_from_csv, read_transactions_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state_and_date, sort_by_date
from src.utils import convert_amount_to_rub, load_financial_transactions
from src.widget import format_date, mask_info
from typing import List, Dict, Tuple


def file_format() -> Tuple[List[Dict], str]:
    """Спрашивает у пользователя какой формат файла нужен"""
    print("Добро пожаловать в программу работы с банковскими транзакциями!")
    while True:
        file = input("Выберите формат файла: 1. Json 2. CSV 3. Excel\n")

        if file == "1":
            print("Для обработки выбран json файл.")
            return (
                load_financial_transactions("C:\\Users\\Student Free\\Desktop\\10.1homework\\data\\operations.json"),
                "json",
            )
        elif file == "2":
            print("Для обработки выбран csv файл.")
            return read_transactions_from_csv("data/transactions.csv"), "csv"
        elif file == "3":
            print("Для обработки выбран excel файл.")
            return read_transactions_from_excel("data/transactions_excel.xlsx"), "excel"
        else:
            print("Пожалуйста, выберите правильный номер опции.")


def filter_status(data_state: List[Dict]) -> List[Dict]:
    """Сортирует список транзакций по статусу"""
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    status = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
    status = status.upper()

    if status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        print(f"Статус операции {status} недоступен, попробуйте снова")
        return filter_status(data_state)

    return filter_by_state_and_date(data_state, status)


def sort_date_currency(data: List[Dict], file: str) -> List[Dict]:
    """Сортирует список транзакций по дате и валюте"""
    sort = input("Отсортировать операции по дате? Да/Нет\n")
    if sort.upper() == "ДА":
        increase = input("Отсортировать по возрастанию или по убыванию?\n")
        if increase.upper() == "ВОЗРАСТАНИЮ":
            data = sort_by_date(data)
        elif increase.upper() == "УБЫВАНИЮ":
            data = sort_by_date(data, "reverse")
        else:
            print("Некорректное значение, повторите ввод")
            return sort_date_currency(data, file)
    elif sort.upper() == "НЕТ":
        pass
    else:
        print("Некорректный ответ, повторите ввод.")
        return sort_date_currency(data, file)

    sort = input("Выводить только рублевые транзакции? Да/нет \n")
    if sort.upper() == "ДА":
        return filter_by_currency(data, "RUB")
    elif sort.upper() == "НЕТ":
        return data
    else:
        print("Некорректное значение, повторите ввод")
        return sort_date_currency(data, file)


def display_transactions(transactions: List[Dict]) -> None:
    """Отображение списка транзакций."""
    transactions_list = list(transactions)
    total_transactions = len(transactions_list)

    if total_transactions:
        print(f"Количество операций: {total_transactions}\n")

        for transaction in transactions_list:
            transaction_date = format_date(transaction["date"])
            transaction_description = transaction["description"]
            transaction_amount = convert_amount_to_rub(transaction)

            print(transaction_date)

            if "Перевод" in transaction_description:
                from_account = mask_info(transaction["from"])
                to_account = mask_info(transaction["to"])
                print(f"{from_account} -> {to_account}")
            else:
                account_info = mask_info(transaction["to"])
                print(account_info)

            print(f"Сумма: {transaction_amount} руб.\n")
    else:
        print("Подходящих транзакций не найдено.")


def main() -> None:
    """Главная функция программы, запускающая обработку транзакций."""
    data, file_type = file_format()
    data = filter_status(data)
    data = sort_date_currency(data, file_type)
    display_transactions(data)


if __name__ == "__main__":
    main()

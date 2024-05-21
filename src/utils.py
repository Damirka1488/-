import json
import os
from typing import Dict, Union, Any, List
import requests


def load_financial_transactions(file_path: str) -> List[Dict]:
    """Функция для чтения данных о финансовых транзакциях из JSON-файла."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not isinstance(data, list):
        return []

    return data


# Пример
if __name__ == "__main__":
    file_path_1 = os.path.join('data', 'operations.json')
    transactions = load_financial_transactions(file_path_1)
    print(transactions)


def convert_amount_to_rub(transaction_sum: Dict[str, Any]) -> Union[float, None]:
    """Функция для конвертации суммы транзакции в рубли."""
    amount = transaction_sum.get('amount', 0)
    currency = transaction_sum.get('currency', 'RUB').upper()

    if currency == 'RUB':
        return amount
    if currency not in ['USD', 'EUR']:
        return None

    url = f'https://api.exchangerate-api.com/v4/latest/{currency}'

    response = requests.get(url)
    data = response.json()

    if 'rates' not in data:
        return None

    rate = data['rates'].get('RUB', 1)
    converted_amount = amount * rate

    return float(converted_amount)


# Пример
if __name__ == "__main__":
    transaction = {
        'amount': 100,
        'currency': 'USD'
    }
    rub_amount = convert_amount_to_rub(transaction)
    print(rub_amount)
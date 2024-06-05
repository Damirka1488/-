from random import randint
from typing import Any, Dict, Generator, Iterator, List


def filter_by_currency(transactions_item: list[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор принимает список словарей с банковскими операциями и код валюты.
    Возвращает операции с указанным кодом валюты.
    """
    for transaction_item in transactions_item:
        if transaction_item["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction_item


# Примеры
transactions = [
    {"id": 939719570, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    {"id": 142264268, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    {"id": 873106923, "operationAmount": {"currency": {"name": "RUB", "code": "RUB"}}},
    {"id": 895315941, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
]


def transaction_descriptions(transactions_translate: List[dict]) -> Generator[str, None, None]:
    """
    Генератор, возвращающий описания транзакций.
    """
    for transaction_translate in transactions_translate:
        yield transaction_translate["description"]


# Примеры
transactions = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Перевод со счета на счет"},
    {"id": 3, "description": "Перевод со счета на счет"},
    {"id": 4, "description": "Перевод с карты на карту"},
    {"id": 5, "description": "Перевод организации"},
]

descriptions = transaction_descriptions(transactions)


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт, в формате "XXXX XXXX XXXX XXXX".
    """
    for _ in range(start, end + 1):
        generated_card_number = "".join(str(randint(1, 9)) for _ in range(16))
        yield " ".join(generated_card_number[i: i + 4] for i in range(0, len(generated_card_number), 4))

from random import randint
from typing import Any, Dict, Generator, Iterator, List


def filter_by_currency(transactions_item: list[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    for transaction_item in transactions_item:
        if transaction_item["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction_item


def test_filter_by_currency() -> None:
    """Проверяет генератор на правильность указания кода валюты"""
    transactions = [
        {"id": 939719570, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
        {"id": 142264268, "operationAmount": {"currency": {"name": "EUR", "code": "EUR"}}},
        {"id": 873106923, "operationAmount": {"currency": {"name": "RUB", "code": "RUB"}}},
        {"id": 895315941, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    ]

    filtered_transactions = list(filter_by_currency(transactions, "USD"))
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in filtered_transactions)
    assert len(filtered_transactions) == 2


def transaction_descriptions(transactions_translate: List[dict]) -> Generator[str, None, None]:
    for transaction_translate in transactions_translate:
        yield transaction_translate["description"]


def test_transaction_descriptions() -> None:
    """Тестирует генератор транзакций на правильность описаний."""
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод с карты на карту"},
        {"id": 5, "description": "Перевод организации"},
    ]

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected_descriptions


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    for _ in range(start, end + 1):
        generated_card_number = "".join(str(randint(1, 9)) for _ in range(16))
        yield " ".join(generated_card_number[i: i + 4] for i in range(0, len(generated_card_number), 4))


def test_card_number_generator() -> None:
    """Тестирует генератор номеров банковских карт на соответствие формату, количеству и уникальности."""
    start, end = 1, 5
    generated_numbers = list(card_number_generator(start, end))
    for number in generated_numbers:
        assert len(number) == 19 and number.count(" ") == 3 and all(part.isdigit() for part in number.split())
    assert len(generated_numbers) == end - start + 1
    assert len(set(generated_numbers)) == len(generated_numbers)

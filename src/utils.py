import json
import os
from typing import Dict, List

from dotenv import load_dotenv

from src.external_api import currency_rate
from src.logger import setup_logging

logger = setup_logging()

load_dotenv()

API_KEY = os.getenv("api_key")


def load_financial_transactions(file_path: str) -> List[Dict]:
    """Функция для чтения данных о финансовых транзакциях из JSON-файла."""
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            logger.error("Файл с транзакциями не найден или пуст")
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info("Данные успешно выведены в консоль")
            return data
        else:
            logger.error("Данные не являются списком")
            return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка чтения JSON-файла: {e}")
        return []


# Пример
if __name__ == "__main__":
    transactions = load_financial_transactions("data/operations.json")
    print(transactions)


def convert_amount_to_rub(transaction: Dict) -> float:
    """Сумма всех транзакции."""
    total = 0.0
    amount = float(transaction.get("operationAmount", {}).get("amount", 0.0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if currency == "RUB":
        total += amount
    elif currency == "USD":
        total += amount * currency_rate("USD")
    elif currency == "EUR":
        total += amount * currency_rate("EUR")
    else:
        logger.error(f"Неизвестная валюта: {currency}")
    logger.info(f"Сумма транзакции: {total} RUB")
    return total


# Пример
if __name__ == "__main__":
    total_sum = convert_amount_to_rub(
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        }
    )
    print(total_sum)

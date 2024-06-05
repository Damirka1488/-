from typing import List, Dict, Any, Set
import re


def search_transactions_by_description(transactions_des: List[Dict[str, Any]], by_search_string: str) -> (
        List)[Dict[str, Any]]:
    result = []
    pattern = re.compile(by_search_string, re.IGNORECASE)
    for transaction in transactions_des:
        if pattern.search(transaction["description"]):
            result.append(transaction)
    return result


def count_transactions_by_category(transactions_cat: List[Dict[str, Any]], by_categories: Set[str]) -> Dict[str, int]:
    category_counts = {category: 0 for category in by_categories}
    for transaction_cat in transactions_cat:
        category = transaction_cat.get("category", "Uncategorized")
        category_counts[category] += 1
    return category_counts


transactions = [
    {"description": "Покупка продуктов", "category": "Питание"},
    {"description": "Оплата коммунальных услуг", "category": "ЖКХ"},
    {"description": "Покупка билетов в кино", "category": "Развлечения"},
    {"description": "Покупка книги", "category": "Развлечения"},
    {"description": "Оплата интернета", "category": "ЖКХ"},
]

search_string = "Покупка"
result_search = search_transactions_by_description(transactions, search_string)
print(result_search)

categories = {"Питание", "ЖКХ", "Развлечения"}
result_count = count_transactions_by_category(transactions, categories)
print(result_count)

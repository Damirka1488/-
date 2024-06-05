from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> list:
    """Чтение финансовых операций из CSV-файла."""
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path, encoding="utf-8")
        transactions_list_csv = df.to_dict(orient="records")
        return transactions_list_csv
    else:
        print("Неверный формат файла CSV.")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """Чтение финансовых операций из XLSX-файла."""
    df = pd.read_excel(file_path)
    transactions_list_excel = df.to_dict(orient="records")
    return transactions_list_excel


# Пример использования
operations_excel = read_transactions_from_excel("data/transactions_excel.xlsx")
operations_csv = read_transactions_from_csv("data/transactions.csv")

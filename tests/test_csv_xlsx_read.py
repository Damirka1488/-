import unittest
from typing import Any
from unittest.mock import Mock, patch

from src.csv_xlsx_read import read_transactions_from_csv, read_transactions_from_excel


class TestReadTransactionsFunctions(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv(self, mock_read_csv: Any) -> None:
        mock_read_csv.return_value = Mock(
            to_dict=lambda orient: [{"date": "2022-01-01", "amount": 100.0}, {"date": "2022-01-02", "amount": 150.0}]
        )

        transactions = read_transactions_from_csv("test.csv")
        self.assertEqual(
            transactions, [{"date": "2022-01-01", "amount": 100.0}, {"date": "2022-01-02", "amount": 150.0}]
        )

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel(self, mock_read_excel: Any) -> None:
        mock_read_excel.return_value = Mock(
            to_dict=lambda orient: [{"date": "2022-01-01", "amount": 100.0}, {"date": "2022-01-02", "amount": 150.0}]
        )

        transactions = read_transactions_from_excel("test.xlsx")
        self.assertEqual(
            transactions, [{"date": "2022-01-01", "amount": 100.0}, {"date": "2022-01-02", "amount": 150.0}]
        )


if __name__ == "__main__":
    unittest.main()

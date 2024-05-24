import unittest
from typing import Any
from unittest.mock import patch, MagicMock
from src.utils import convert_amount_to_rub, load_financial_transactions


class TestConvertAmountToRUB(unittest.TestCase):

    @patch("requests.get")
    def test_convert_amount_to_rub_usd(self, mock_get: Any) -> None:
        mock_response = mock_get.return_value
        mock_response.json.return_value = {"rates": {"RUB": 75}}

        transaction = {"amount": 100, "currency": "USD"}
        rub_amount = convert_amount_to_rub(transaction)
        self.assertEqual(rub_amount, 7500.0)

    @patch("requests.get")
    def test_convert_amount_to_rub_invalid_currency(self, mock_get: Any) -> None:
        mock_response = mock_get.return_value
        mock_response.json.return_value = {}

        transaction = {"amount": 100, "currency": "JPY"}
        rub_amount = convert_amount_to_rub(transaction)
        self.assertIsNone(rub_amount)

    @unittest.mock.patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_load_financial_transactions_file_opened(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = (
            '[{"transaction_id": 1, "amount": 100},' ' {"transaction_id": 2, "amount": 200}]'
        )

    result = load_financial_transactions("test.json")
    expected_result = [{"transaction_id": 1, "amount": 100}, {"transaction_id": 2, "amount": 200}]


if __name__ == "__main__":
    unittest.main()

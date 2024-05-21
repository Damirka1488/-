import unittest
from unittest.mock import patch
from src.utils import convert_amount_to_rub
from typing import Any


class TestConvertAmountToRUB(unittest.TestCase):

    @patch('requests.get')
    def test_convert_amount_to_rub_usd(self, mock_get: Any) -> None:
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'rates': {'RUB': 75}}

        transaction = {'amount': 100, 'currency': 'USD'}
        rub_amount = convert_amount_to_rub(transaction)
        self.assertEqual(rub_amount, 7500.0)

    @patch('requests.get')
    def test_convert_amount_to_rub_invalid_currency(self, mock_get: Any) -> None:
        mock_response = mock_get.return_value
        mock_response.json.return_value = {}

        transaction = {'amount': 100, 'currency': 'JPY'}
        rub_amount = convert_amount_to_rub(transaction)
        self.assertIsNone(rub_amount)


if __name__ == '__main__':
    unittest.main()

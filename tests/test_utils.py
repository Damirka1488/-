import unittest
from unittest.mock import MagicMock, patch

from src.utils import convert_amount_to_rub, load_financial_transactions


class TestConvertAmountToRub(unittest.TestCase):

    @patch("src.utils.currency_rate")
    def test_convert_amount_to_rub(self, mock_currency_rate: MagicMock) -> None:
        mock_currency_rate.return_value = 70.0

        test_transaction = {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        }

        total_sum = convert_amount_to_rub(test_transaction)

        self.assertEqual(total_sum, 43318.34)

    @unittest.mock.patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_load_financial_transactions_file_opened(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = (
            '[{"transaction_id": 1, "amount": 100},' ' {"transaction_id": 2, "amount": 200}]'
        )

    result = load_financial_transactions("test.json")
    expected_result = [{"transaction_id": 1, "amount": 100}, {"transaction_id": 2, "amount": 200}]


if __name__ == "__main__":
    unittest.main()

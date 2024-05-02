import pytest
from src.masks import mask_account_number, mask_card_number


@pytest.mark.parametrize("account_number, expected_result", [
    ("1234567890", "Счет **7890"),
    ("9876543210", "Счет **3210"),
    ("0000123456", "Счет **3456"),
])
def test_mask_account_number(account_number, expected_result):
    assert mask_account_number(account_number) == expected_result


@pytest.mark.parametrize("card_number, expected_result", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("9876543210987654", "9876 54** **** 7654"),
    ("0000111122223333", "0000 11** **** 3333"),
])
def test_mask_card_number(card_number, expected_result):
    assert mask_card_number(card_number) == expected_result
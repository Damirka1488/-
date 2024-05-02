from src.widget import mask_info, format_date


def test_mask_info():
    assert mask_info("Счет 1234567890") == "Счет **7890"
    assert mask_info("Maestro 1234567890123456") == "Maestro 1234 56** **** 3456"


def test_format_date():
    assert format_date("2018-07-11T02:26:18.671407") == "11.07.2018"
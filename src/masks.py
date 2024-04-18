def mask_account_number(account_number: str) -> str:
    """Возвращает замаскированный номер счета в формате **XXXX."""

    last_four = account_number[-4:]
    masked_number = "Счет " + "**" + last_four
    return masked_number


def mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX."""

    first_six = card_number[:4]
    average_two = card_number[4:6]
    last_four = card_number[-4:]
    masked_number = first_six + " " + average_two + "** **** " + last_four
    return masked_number

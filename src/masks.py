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


def mask_info(info: str) -> str:
    """Возвращает номер карты или номер счёта"""
    if info.startswith('Счет'):
        return mask_account_number(info.split()[1])
    elif info.startswith('Mastercard'):
        return 'Mastercard ' + mask_card_number(info.split()[1])
    elif info.startswith('Maestro'):
        return 'Maestro ' + mask_card_number(info.split()[1])
    else:
        return ' '.join([info.split()[0]] + [mask_card_number(num) if i == 1 else num for i, num in enumerate(info.split
                                                                                                              ()[1:])])

def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date

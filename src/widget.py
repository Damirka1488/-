from datetime import datetime

from src.masks import mask_account_number, mask_card_number


def mask_info(info: str) -> str:
    """Возвращает номер карты или номер счёта"""
    if info.startswith("Счет"):
        return mask_account_number(info.split()[1])
    elif info.startswith("Mastercard"):
        return "Mastercard " + mask_card_number(info.split()[1])
    elif info.startswith("Maestro"):
        return "Maestro " + mask_card_number(info.split()[1])
    else:
        return " ".join(
            [info.split()[0]] + [mask_card_number(num) if i == 1 else num for i, num in enumerate(info.split()[1:])]
        )


def format_date(date_str: str) -> str:
    """Получает дату в формате 2018-07-11T02:26:18.671407 и выводит 11.07.2018"""
    try:
        # Попытка обработать дату с микросекундами
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        # Попытка обработать дату без микросекунд, если предыдущий формат не подошёл
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

        # Форматирование даты в формат DD.MM.YYYY
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date

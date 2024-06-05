from src.logger import setup_logging

logger = setup_logging()


def mask_account_number(account_number: str) -> str:
    """Возвращает замаскированный номер счета в формате **XXXX."""
    if len(account_number) >= 4:
        last_four = account_number[-4:]
        masked_number = "Счет " + "**" + last_four
        logger.info("Функция mask_card работает правильно")
        return masked_number
    else:
        logger.error("Функция mask_account_nuber работает неправильно")
        return "Неправильный номер счета"


def mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX."""
    if len(card_number) == 16:
        first_six = card_number[:4]
        average_two = card_number[4:6]
        last_four = card_number[-4:]
        masked_number = first_six + " " + average_two + "** **** " + last_four
        logger.info("Функция mask_card_number работает правильно")
        return masked_number
    else:
        logger.error("Функция mask_card_number работает неприавильно")
        return "Неправильный номер карты"

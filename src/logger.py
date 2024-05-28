import logging
from typing import Any


def setup_logging() -> Any:
    """Настройка логгирования."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_processing = logging.FileHandler("app.log", mode="w")
    file_processing.setFormatter(formatter)
    logger.addHandler(file_processing)
    return logger

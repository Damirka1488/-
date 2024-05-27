import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("api_key")


def currency_rate(currency: Any) -> float:
    """Получает курс валюты API"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    response = requests.get(url, headers={"apikey": API_KEY}, timeout=5)
    response.raise_for_status()
    response_data = response.json()
    rate = response_data["rates"]["RUB"]

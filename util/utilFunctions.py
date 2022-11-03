from decimal import Decimal
from re import sub
import secrets


def convert_currency_to_float(currency):
    value = Decimal(sub(r'[^\d.]', '', currency))
    return float(int(value * 1000))


def get_random_value():
    random = str(secrets.randbelow(1_000_000_000))
    return random
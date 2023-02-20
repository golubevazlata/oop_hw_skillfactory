import requests
import json
from config import values


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'введены одинаковые валюты: {base}-{quote}')

        try:
            base_ticker = values[base]
        except KeyError:
            raise APIException(f'неизвестная валюта {base}')

        try:
            quote_ticker = values[quote]
        except KeyError:
            raise APIException(f'неизвестная валюта {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'значение количества не является числом {amount}')

        if amount <= 0:
            raise APIException(f'значение количества не положительное число {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        result = json.loads(r.content)[values[quote]]
        result *= amount

        return result

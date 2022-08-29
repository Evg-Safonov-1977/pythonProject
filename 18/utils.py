import requests
from config import keys


class APIException(Exception):
    pass

class ValConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except KeyError:
            raise APIException(f'Не удалось обработать количество {amount}')

        # r = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}")
        # total_base = json.loads(r.content)[keys[base]]
        #
        # return total_base

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"

        payload = {}
        headers = {"apikey": "DjzPoQ4twiNmuz5WhZClmbG49vhzMu1U"}

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.text
        print(result)
        return result

        # result = json.loads(response.content)[keys[base]]
        # return total_base
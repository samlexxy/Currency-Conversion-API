import os
import requests
from dotenv import load_dotenv

load_dotenv()

def convert(type, payload = None):
    if type == 'convert' and payload:
        to_currency = payload['to']
        from_currency = payload['from']
        amount = payload['amount']
        url = f'https://xecdapi.xe.com/v1/convert_from/?from={from_currency}&to={to_currency}&amount={amount}'
    elif type == 'currencies':
        url = 'https://xecdapi.xe.com/v1/currencies/'
    payload={}
    headers = {
    'Authorization': f"Basic {os.getenv('XDCI_API_KEY')}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
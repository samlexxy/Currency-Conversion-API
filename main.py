from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN
import auth, xdci_api

app = FastAPI()
conversations = []

@app.get("/convert")
async def get_convert(amount: float, from_currency: str, to_currency: str, api_key: APIKey = Depends(auth.get_api_key)):
    data = xdci_api.convert('convert', {'amount': amount, 'to': to_currency, 'from': from_currency})
    try:
        converted_amount = round(data['to'][0]['mid'], 4)
    except:
        return {'Error' : 'Currency Information Not Found'}

    rate = round(converted_amount / amount, 4)
    time_of_conversion = data['timestamp']

    conversations.append({
            'converted_amount': converted_amount,
            'rate': rate,
            'metadata': {
                'time_of_conversion': time_of_conversion,
                'from_currency': from_currency,
                'to_currency': to_currency
            }}
        )

    return  {
        "converted_amount": converted_amount, 
        "rate": rate, 
        "metadata": {
            "time_of_conversion": time_of_conversion, 
            "from_currency": from_currency, 
            "to_currency": to_currency,
        }}


@app.get("/currencies")
async def get_currencies(api_key: APIKey = Depends(auth.get_api_key)):
    data = xdci_api.convert('currencies')
    item_dict = {}
    try:
        if data['currencies']:
            for currency in data['currencies']:
                item_dict.update(
                    {currency['currency_name']: currency['iso']}
                )
    except:
        if data.get('code') == 9:
            item_dict = {'Error': 'Expired API KEY'}
    return item_dict


@app.get("/history")
async def read_history(api_key: APIKey = Depends(auth.get_api_key)):
    return conversations
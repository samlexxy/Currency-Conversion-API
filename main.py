import requests
from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN


def xecdapi_call(type, payload = None):
    if type == 'convert' and payload:
        to_currency = payload['to']
        from_currency = payload['from']
        amount = payload['amount']
        url = f'https://xecdapi.xe.com/v1/convert_from/?from={from_currency}&to={to_currency}&amount={amount}'
    elif type == 'currencies':
        url = 'https://xecdapi.xe.com/v1/currencies/'
    payload={}
    headers = {
    'Authorization': 'Basic Y29yZXNpZ2h0ODYwOTE4NTMxOmNvM2dhMmNmN201YzZkaGlmbnZwNjdwZDk3'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


app = FastAPI()
api_keys = [
    "3JSkskkd044kSKDKDKDKK8888D",
] 

conversations = []


api_key_header = APIKeyHeader(name="access_token", auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header in api_keys:
        return api_key_header   
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )



@app.get("/convert")
async def get_convert(amount: float, from_currency: str, to_currency: str, api_key: APIKey = Depends(get_api_key)):
    data = xecdapi_call('convert', {'amount': amount, 'to': to_currency, 'from': from_currency})
    try:
        converted_amount = round(data['to'][0]['mid'], 4)
    except:
        return {}
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
async def get_currencies(api_key: APIKey = Depends(get_api_key)):
    data = xecdapi_call('currencies')
    item_dict = {}

    if data['currencies']:
        for currency in data['currencies']:
            item_dict.update(
                {currency['currency_name']: currency['iso']}
            )
    return item_dict


@app.get("/history")
async def read_history(api_key: APIKey = Depends(get_api_key)):
    return conversations
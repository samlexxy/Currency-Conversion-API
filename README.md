**Currency Conversion API**

This API is built using FastAPI and allows for conversion of currency 
using the xecdAPI.

**Endpoints**

`/convert`: This endpoint allows you to convert a certain amount of 
one currency to another
`/currencies`: This endpoint returns a list of currencies and their 
corresponding iso codes
`/history`: This endpoint returns a list of all previously made 
conversions

**Getting Started**
1. Clone the repository

`$ git clone https://github.com/yourusername/currency-conversion-api.git`

2. Install the dependencies

`$ pip install -r requirements.txt`

3. Run the application

`$ uvicorn main:app --reload`

4. Test the endpoints

The endpoints are protected by API key auth. To access the endpoints, 
you will need to add the key to the headers of your requests.

`/convert`:
    Endpoint example: http://localhost:8000/convert?amount=1&from_currency=USD&to_currency=NGN
    Request example: GET http://localhost:8000/convert?amount=1&from_currency=USD&to_currency=NGN
    Headers example: access_token: 3JSkskkd044kSKDKDKDKK8888D
    
`/currencies`:
    Endpoint example: http://localhost:8000/currencies
    Request example: GET http://localhost:8000/currencies
    Headers example: access_token: 3JSkskkd044kSKDKDKDKK8888D
    
`/history`:
    Endpoint example: http://localhost:8000/history
    Request example: GET http://localhost:8000/history
    Headers example: access_token: 3JSkskkd044kSKDKDKDKK8888D

Note
* Make sure you have internet connection as the API relies on the xecdAPI 
to convert currency.
* You can edit the api_keys list in main.py to include your own API key.
* Endpoints are protected with API key auth, so make sure to include 
the access_token in the headers of your requests.

**API documentation**

The API documentation can be accessed by running the app and visiting
 `http://localhost:8000/docs` on your browser.

**Dependencies**

This API uses the following dependencies:
* FastAPI
* requests

**Deployment**

This API can be deployed on a server of your choice (e.g. Heroku, AWS) 
and can be accessed by replacing `http://localhost:8000` with the server's URL.

**Contributions**

We welcome contributions to this project. If you have an idea for an improvement, 
please open an issue or submit a pull request.

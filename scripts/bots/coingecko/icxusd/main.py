#!/usr/bin/env python
import requests
import json

URL = "https://api.coingecko.com/api/v3/coins/icon?localization=false"

if __name__ == '__main__':
    try:
        tickers = json.loads(requests.get(URL).text)
        current_price = tickers['market_data']['current_price']['usd']
        price = float(current_price)
        print(int(1 / price * 10**18))
    except:
        print(0)
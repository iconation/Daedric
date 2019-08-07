#!/usr/bin/env python
import requests
import json

TICKER = "icon"
URL = "https://api.coinmarketcap.com/v1/ticker/%s/" % TICKER

if __name__ == '__main__':
    try:
        result = json.loads(requests.get(URL).text)
        price = float(result[0]["price_usd"])
        print(int(1 / price * 10**18))
    except:
        print(0)

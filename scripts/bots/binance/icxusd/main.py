#!/usr/bin/env python
import requests
import json

TICKER = "ICXUSDT"
URL = "https://api.binance.com/api/v1/ticker/24hr?symbol=%s" % TICKER

if __name__ == '__main__':
    try:
        result = json.loads(requests.get(URL).text)
        price = float(result["lastPrice"])
        print(int(1 / price * 10**18))
    except:
        print(0)

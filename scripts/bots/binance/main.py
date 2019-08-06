#!/usr/bin/env python
import requests
import json

if __name__ == '__main__':
    result = json.loads(requests.get("https://api.binance.com/api/v1/ticker/24hr?symbol=ICXUSDT").text)
    price = float(result["lastPrice"])
    print(int(1 / price * 10**18))

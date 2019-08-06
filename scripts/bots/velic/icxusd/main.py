#!/usr/bin/env python
import requests
import json

BASE_COIN = "USDT"
MATCH_COIN = "ICX"
URL = "https://api.velic.io/api/v1/public/ticker/"

if __name__ == '__main__':
    try:
        tickers = json.loads(requests.get(URL).text)
        result = list(filter(
            lambda ticker:
                ticker['base_coin'] == BASE_COIN and
                ticker['match_coin'] == MATCH_COIN,
            tickers
        ))[0]
        price = float(result["recent_price"])
        print(int(1 / price * 10**18))
    except:
        print(0)

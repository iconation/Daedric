#!/usr/bin/env python
import requests
import json
import sys

if __name__ == '__main__':
    try:
        prices = [int(arg) for arg in sys.argv[1:]]
        candidates = list(filter(lambda price: price != 0, prices))
        # Arithmetic mean
        print(int(sum(candidates) / len(candidates)))
    except:
        print(0)

#!/usr/bin/env python
import requests
import json
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]

    if argv:
        prices = [int(arg) for arg in argv]
        candidates = list(filter(lambda price: price != 0, prices))
        # Arithmetic mean
        print(int(sum(candidates) / len(candidates)))

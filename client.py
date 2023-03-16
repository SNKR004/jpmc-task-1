import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    if price_b == 0:
        return
    return price_a/price_b

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        for i in quotes:
            stock, bid_price, ask_price, price = getDataPoint(i)
            print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")
        print(f"Ratio {getRatio(price['ABC'],price['DEF'])}")

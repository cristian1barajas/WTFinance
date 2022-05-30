import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import parameters as params

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

headers = {
    'X-CMC_PRO_API_KEY': 'bac6a411-1c84-449e-9588-4937c3bcb943',
    'Accepts': 'application/json'
}

def getDataBTC():
    try:
        json = requests.get(url, params=params.paramsBTC, headers = headers).json()
        coinData = json['data']['BTC']
        price = str(round(coinData['quote']['USD']['price'], 5))
        percentChange = str(round(coinData['quote']['USD']['percent_change_24h'], 2))
        #print(json)
        print("Symbol: BTC Price: " + price + " Percent change 24h: " + percentChange)
        items = ("BTC", price, percentChange)
        return items
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def getDataETH():
    try:
        json = requests.get(url, params=params.paramsETH, headers = headers).json()
        coinData = json['data']['ETH']
        price = str(round(coinData['quote']['USD']['price'], 5))
        percentChange = str(round(coinData['quote']['USD']['percent_change_24h'], 2))
        #print(json)
        print("Symbol: ETH Price: " + price + " Percent change 24h: " + percentChange)
        items = ("ETH", price, percentChange)
        return items
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def getDataUSDT():
    try:
        json = requests.get(url, params=params.paramsUSDT, headers = headers).json()
        coinData = json['data']['USDT']
        price = str(round(coinData['quote']['USD']['price'], 5))
        percentChange = str(round(coinData['quote']['USD']['percent_change_24h'], 2))
        #print(json)
        print("Symbol: USDT Price: " + price + " Percent change 24h: " + percentChange)
        items = ("USDT", price, percentChange)
        return items
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def getDataUSDC():
    try:
        json = requests.get(url, params=params.paramsUSDC, headers = headers).json()
        coinData = json['data']['USDC']
        price = str(round(coinData['quote']['USD']['price'], 5))
        percentChange = str(round(coinData['quote']['USD']['percent_change_24h'], 2))
        #print(json)
        print("Symbol: USDC Price: " + price + " Percent change 24h: " + percentChange)
        items = ("USDC", price, percentChange)
        return items
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def getDataBNB():
    try:
        json = requests.get(url, params=params.paramsBNB, headers = headers).json()
        coinData = json['data']['BNB']
        price = str(round(coinData['quote']['USD']['price'], 5))
        percentChange = str(round(coinData['quote']['USD']['percent_change_24h'], 2))
        #print(json)
        print("Symbol: BNB Price: " + price + " Percent change 24h: " + percentChange)
        items = ("BNB", price, percentChange)
        return items
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
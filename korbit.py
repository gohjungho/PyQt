import requests
import datetime

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

bitcoin = r.json()
print(bitcoin)
print(type(bitcoin))

print()

print(bitcoin['last'])
print(bitcoin['open'])
print(bitcoin['bid'])
print(bitcoin['ask'])
print(bitcoin['low'])
print(bitcoin['high'])
print(bitcoin['volume'])
print(bitcoin['change'])
print(bitcoin['changePercent'])

print()

timestamp = bitcoin['timestamp']
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)
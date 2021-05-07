# 이동평균을 비교해 상승장/하락장 구분하기 

import pybithumb 

df = pybithumb.get_ohlcv("BTC")
ma5 = df['close'].rolling(window=5).mean()
last_ma5 = ma5[-2]

price = pybithumb.get_current_price("BTC")

if price > last_ma5:
    print("상승장")
else: 
    print("하락장")
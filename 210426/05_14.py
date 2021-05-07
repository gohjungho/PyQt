# 과거 종가 확인하기  

import pybithumb 

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']
print(close)
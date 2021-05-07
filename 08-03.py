import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
print(df)

df = pyupbit.get_ohlcv("KRW-XRP", interval="minute")
print(df)
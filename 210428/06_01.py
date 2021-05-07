import pybithumb
import time

con_key = "e30670cba74f0c5b6515ea7c97e37e89"
sec_key = "1f89a64488f5431a6b62e43314f11ff0"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# balance = bithumb.get_balance("BTC")
# print(balance)

for ticker in pybithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)
import pybithumb
import time

con_key = "e30670cba74f0c5b6515ea7c97e37e89"
sec_key = "1f89a64488f5431a6b62e43314f11ff0"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 비트코인 1개를 100,000,000원에 지정가 매도하기 
order = bithumb.sell_limit_order("BTC", 100000000, 1)
print(order)


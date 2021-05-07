import pybithumb

con_key = "e30670cba74f0c5b6515ea7c97e37e89"
sec_key = "1f89a64488f5431a6b62e43314f11ff0"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 100원 단위로 주문하기 - 오류(비트코인은 1,000원 단위로 호가를 지정해야 함)
# order = bithumb.buy_limit_order("BTC", 4000100, 0.001)
# print(order)

# 06_05.py
# 시장가로 비트코인 1개를 매수하기 
# order = bithumb.buy_market_order("BTC", 1)
# print(order)


# 06_06.py 
# # 본인 계좌의 보유 원화를 조회하고, 최우선 매도 호가 금액을 얻어와 매수할 수 있는 비트코인 개수를 계산
krw = bithumb.get_balance("BTC")[2]
orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw / sell_price
print(unit)
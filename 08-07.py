import pyupbit

access_key = "DAk9rXqPvfit5BUFspEH8KgTDR7xzroPT60hSCjx"
secret_key = "5kpg2xcaPWx7MujjVMjN9PEvXMfHq7Rvxf5zuete"

upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.buy_limit_order("KRW-XRP", 100, 20)
print(ret)
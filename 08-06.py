import pyupbit

access_key = "DAk9rXqPvfit5BUFspEH8KgTDR7xzroPT60hSCjx"
secret_key = "5kpg2xcaPWx7MujjVMjN9PEvXMfHq7Rvxf5zuete"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())
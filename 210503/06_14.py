import datetime
import time

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

while 1:
    now = datetime.datetime.now()
    if now == mid :
        print("정각입니다. ")
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    print(now, "vs", mid)
    time.sleep(1)
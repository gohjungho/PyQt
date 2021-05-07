import datetime

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

print(now) # 날짜는 곧 시간 개념. 비교 가능 
print(mid)
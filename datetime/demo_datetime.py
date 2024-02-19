from datetime import datetime, timedelta

# datetime转字符串
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 字符串转datetime
print(datetime.strptime("2022-01-01", "%Y-%m-%d"))

# 时间修改
print(datetime.now() + timedelta(hours= 1))

# 时间戳
print(int(datetime.now().timestamp() * 1000))

# 时间戳
print(datetime.utcnow().timestamp())
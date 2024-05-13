from datetime import timedelta
from datetime import datetime, timezone
import time

print("timestamp: ", time.time())
print("time.strftime: ", time.strftime("%Y-%m-%d"))
print("time.strftime: ", time.strftime("%Y-%m-%d %H:%M:%S"))


# 1. current time
now = datetime.now()
print("datetime.now: ", now)

# 2. 获取特定格式的时间字符串
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("now.strftime: ", formatted_now)

# 3. 解析特定格式时间
date_str = "2024-06-01 12:13:14"

parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


# 4. 时间戳转换为时间
timestamp = time.time()
timestamp_datetime = datetime.fromtimestamp(timestamp)
print("时间戳转换为时间：", timestamp_datetime)

# 5. 格式化时间差

# 创建一个时间差对象
time_delta = timedelta(days=2, hours=6, minutes=30)

# 格式化时间差
delta_str = time_delta.total_seconds()
print(f"时间差（秒）：{delta_str}")

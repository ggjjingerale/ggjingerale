import datetime


# 指定开始时间
t_str = '2024-09-05 16:26:23'
d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
# 现在时间
d = datetime.datetime.now()


# 计算时间变量
print(d + datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=22))
# 计算时间变量
print(d + datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=22+18))

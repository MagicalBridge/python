# Author:Louis Chu
# 内置的时间模块,有三种形式struct_time
# 格式化字符串
# 时间戳
import time
# x = time.localtime()
#time.struct_time(tm_year=2017, tm_mon=11, tm_mday=2, tm_hour=18, tm_min=15, tm_sec=52, tm_wday=3, tm_yday=306, tm_isdst=0)
# print(x.tm_year) #2017
# print(help(x))




# 如果传入的是一个相应的事件戳  那么可以打印出是当年的第几天
y = time.localtime(12312321)
print(y.tm_year) #1970
print('this is 1973 year %d'%y.tm_yday) #this is 1973 year 143

#将元组的形式转化为秒的形式,使用的mktime这个api
z = time.localtime()
print(z)
print(time.mktime(z)) #1509674262.0 将结构化的元组转化为事件戳


# 格式化字符串  和元组时间格式之间的转化 stiftime
# 第一个参数放的是格式 第二个参数放的是元组的形式
# 这个元组是使用内置模块对象time.localtime 实现的;
# 这是自定义的输出的时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S",z)) #2017-11-03 10:03:45

#time.strptime 将格式化的字符转化成元组的形式
#用法就是将strftime 传入的参数反向输出就行了

print(time.strptime("2017-11-03 10:03:45","%Y-%m-%d %H:%M:%S"))
# time.struct_time(tm_year=2017, tm_mon=11, tm_mday=3, tm_hour=10, tm_min=3, tm_sec=45, tm_wday=4, tm_yday=307, tm_isdst=-1)


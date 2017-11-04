# Author:Louis Chu
import shelve
import datetime

# 下列的代码生成的相应的文件
# d = shelve.open('shelve_test')  # 打开一个文件
# info = {"age": "22", "job": "it"}
# name = ["louis", "rain", "test"]
# d["name"] = name  # 持久化列表
# d["info"] = info  # 持久化类
# d["date"] = datetime.datetime.now()
# d.close()


# 下面的额代码将生成的文件读取出来
d = shelve.open('shelve_test')  # 打开一个文件
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))

# ['louis', 'rain', 'test']
# {'job': 'it', 'age': '22'}
# 2017-11-04 11:05:16.287813
# 将写进去的文件重新读取出来

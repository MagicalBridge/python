# Author:Louis Chu

f = open("yesterday", "r", encoding="utf-8")
# print(f.readlines())  # 将文件分割成整个列表进行操作

# for line in f.readlines():
#     print(line.strip()) #strip 去掉空格和换行

# 第一种循环
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print("-----我是分割线-----")
#         continue
#     print(line.strip())

# 第二种循环
count = 0
for line in f:
    if count == 9:
        print("-----我是分割线-----")
        count += 1
        continue
    print(line.strip())

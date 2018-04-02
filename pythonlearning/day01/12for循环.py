# Author:Louis Chu
# 这是一个简单的for循环 在这个循环中 i 是一个临时的变量
# 这里面的 range 我们可以理解为循环10次。
# 打印的结果是 0-9
# for i in range(10):
#     print("loop", i)

# 打印结果：
# loop 0
# loop 1
# loop 2
# loop 3
# loop 4
# loop 5
# loop 6
# loop 7
# loop 8
# loop 9


# 下面这个for循环增加了 步长 的概念，也就是隔几个打印一下
# 默认的步长是1,可以不写
for j in range(0, 10, 2):
    print("for循环升级版本", j)

# for循环升级版本 0
# for循环升级版本 2
# for循环升级版本 4
# for循环升级版本 6
# for循环升级版本 8

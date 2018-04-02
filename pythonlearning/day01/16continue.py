# Author:Louis Chu


# continue的作用 跳出这次循环继续执行下次循环
# 注意和break的区别，break是结束整个循环
# 看下列的代码逻辑

for i in range(5):
    if i < 3:
        print("loop", i)
    else:
        continue
    print("my name is louis")


# loop 0
# my name is louis
# loop 1
# my name is louis
# loop 2
# my name is louis

# 上述的打印结果很好的说明了continue的作用
# 也就是说,当 i = 3的时候 走的else逻辑
# 直接跳过了 print("my name is louis")
# 继续回到循环

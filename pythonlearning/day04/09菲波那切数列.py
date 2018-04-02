# Author:Louis Chu
# 斐波那契数列的函数的实现里面传入的参数是生成的数列的位数
# 分析一下函数额运行流程；

def fib(max):  # 定义一个fib 函数
    n, a, b = 0, 0, 1  # 初始化三个参数 并分别赋值 n,a,b
    while n < max:  # 执行循环
        print(b)  # 初始化的时候b是1
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(10)

# 执行的过程的如下初始化
# n = 0 n<3   a = b => 1  b = a+b => 1;
# n = 1 n<3   a = b => 1  b= a+b => 2


# 这里的赋值语句相当于
# t = (b, a + b)  # t是一个tuple;
# a = t[0]
# b = t[1]

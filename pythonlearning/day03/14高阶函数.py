# Author:Louis Chu

# 变量可以指向函数，函数的参数能够接收变量 那么
# 一个函数就可以接收另外一个函数作为参数
# 这种函数称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)

res = add(3,-6,abs)
print(res)

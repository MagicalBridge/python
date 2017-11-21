# Author:Louis Chu
# 装饰器
#  本质上是一个函数  (装饰其他的函数)
#  就是为了其他函数添加附加功能;
#
#  原则：1.不能修改被装饰的函数的源代码
#        2.不能修饰的函数的调用方式


# 知识储备
# 1.函数即变量
# 2.高阶函数
#     a.把一个函数名当做实参传递给另外一个函数;
#     b.返回值中包含函数名;
# 3.嵌套函数

#装饰器 = 高阶函数+嵌套函数；






import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return wrapper
@timmer
def test1():
    time.sleep(3)
    print('in the test1')

test1()


# in the test1
# the func run time is 3.000171661376953

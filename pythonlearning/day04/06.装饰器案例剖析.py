# Author:Louis Chu

# 写一个函数的运行时间的装饰器装饰器的构成要素是 高阶函数+
import time
def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print(" the func run time is%s"%(stop_time-start_time))
    return deco
#使用timer调用 调用的时候
@timer
def test1():
    time.sleep(3)
    print("in the func test1")
test1()
# in the func test1
#  the func run time is3.000171661376953
# Author:Louis Chu

# 写一个函数的运行时间的装饰器装饰器的构成要素是 高阶函数+
import time
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print(" the func run time is%s"%(stop_time-start_time))
    return deco
#使用timer调用 调用的时候
@timer
def test1():
    time.sleep(1)
    print("in the func test1")

@timer
def test2(name):
    print("my name is",name)

test1()
test2("louis")

# in the func test1
#  the func run time is1.0000572204589844
# my name is louis
#  the func run time is0.0
# Author:Louis Chu


# def bar():
#     print("in the bar")
#
# def test1(func):
#     print(func)
#     func() # 这里加上一个函数  还是能够运行的,原因是我传入的是一个函数的引用 加上括号就相当于执行了这个函数;
#
# test1(bar) #<function bar at 0x005B66F0>这里打印的是函数的名字 那么执行的结果就是bar 函数所指向的内存地址;


# 使用高阶函数的形式 模拟装饰器的功能
import time
def bar():
    time.sleep(3)
    print("in the bar")

def test(func):

    start_time  = time.time()
    func()
    stop_time = time.time()
    print("the func is end %s"%(stop_time-start_time))
test(bar)
# in the bar
# the func is end 3.000171661376953

# 上面的这种调用方式 只符合装饰器的第一条规则 没有更改原来的
# 函数但是有一点需要需要注意虽然没有修改原来的函数但是
# 不符合第二条规则,已经修改函数的调用方式;
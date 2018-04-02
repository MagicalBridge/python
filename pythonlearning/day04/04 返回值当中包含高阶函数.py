# Author:Louis Chu
import time #导入时间模块

#定义bar 函数 沉睡3秒 打印  我在bar 函数中
def bar():
    time.sleep(3)
    print('in the bar')
#  test函数接收一个函数
def test(func):
    print(func)  #首先打印这个函数的内存地址
    return func #返回这个函数内存地址;


# print(test(bar))
# <function bar at 0x00657E40>
# <function bar at 0x00657E40>

# 使用如下的调用方式将test执行的结果再赋值给一个变量这个变量
# 名为bar 和所调用的函数相同 此时 再进行调用

bar = test(bar)
bar()

# 这个函数能够执行同样的结果;

































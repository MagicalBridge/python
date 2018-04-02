# 通过Event来实现两个或多个线程间的交互，
# 下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，
# 生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则。

import threading,time
import random
def light():
    if not event.isSet():  #如果标志位没有设置 此时进行的设置一个标志位 设置标志位的说明是绿灯
        event.set() #wait就不阻塞 #绿灯状态
    count = 0   #设置计数变量是0
    while True: # 执行一个无限的循环
        if count < 10:  # 当计数标志小于10 的时候 绿灯状态
            print('\033[42;1m--green light on---\033[0m')
        elif count <13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count <20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set() #打开绿灯
        time.sleep(1)
        count +=1
def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if  event.isSet(): #绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." %n)
if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()
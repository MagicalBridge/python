# Author:Louis Chu
# 1.继承的时候分为深度优先和广度优先的为问题
#   在py3中使用的是广度优先的过程
#   在py2中旧式类使用的是深度优先
#   在py2中新式类使用的广度优先的策略


# 创建一个Person类
class People:
    #初始化构造方法 初始化 姓名和年龄
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 定义吃这个方法
    def eat(self):
        print("%s is eating……"%(self.name))
    # 定义睡方法
    def sleep(self):
        print("%s is sleepping……" % (self.name))
    # 定义说话这个方法
    def talk(self):
        print("%s is talking……" % (self.name))

# 创建Man这个类;继承People
class Man(People):
   #定义自己的方法 piao
    def piao(self):
        print("%s is piaoing……20s……done"%(self.name))




#实例化对象传入两个参数 必填否则会报错;
m1 = Man("牛韩阳","22")
#执行eat方法;
m1.eat()
m1.piao()




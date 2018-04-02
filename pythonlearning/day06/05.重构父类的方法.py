# Author:Louis Chu

# 重构父类的方法
#     如果在Man这个类里面定义一个sleep函数 会覆盖父类的sleep函数
#     但是我想实现的功能是 先执行父类的方法 再执行子类的方法
#     在子类中直接调用父类的方法 然后再执行自己的逻辑
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
    def sleep(self):
        People.sleep(self)  # 这里的self 是m1
        print("man is sleep")

#实例化对象传入两个参数 必填否则会报错;
m1 = Man("牛韩阳","22")
#执行eat方法;
m1.eat()
m1.piao()
m1.sleep() # 牛韩阳 is sleep
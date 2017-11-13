# Author:Louis Chu
# 如果我想给man  多添加一个属性 但是不改变 women的属性
# 此时就不能修改people 上面的参数
# 用户初始化实例的时候 首先读取的是man自己的构造函数 _init_
#
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
    def __init__(self,name,age,money):
        People.__init__(self,name,age)  # 先执行父类的方法
        self.money = money # 再执行自己的属性
        print("%s 一出生就有%s钱"%(self.name,self.money))
   #定义自己的方法 piao
    def piao(self):
        print("%s is piaoing……20s……done"%(self.name))
    def sleep(self):
        People.sleep(self)  # 这里的self 是m1
        print("man is sleep")


# 创建Woman 这个类 继承People
class Woman(People):
    # 定义生孩子方法
    def born(self):
        print("%s is born a baby……" % (self.name))

#实例化对象传入两个参数 必填否则会报错;
m1 = Man("牛韩阳","22",10)
#执行eat方法;
m1.eat()
m1.piao()
m1.sleep() # 牛韩阳 is sleep


#实例化 women对象
w1 = Woman("陈荣华","22")
w1.born()
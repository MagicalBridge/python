# Author:Louis Chu
# 多继承使用的是什么 新式类的写法

class People(object):
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


# 创建一个交朋友的类
class Relation(object):
    #这里定义的交朋友的接收的属性还包括 obj obj是一个人具备name 属性
    def makeFriend(self,obj):
        print("%s is making friends with %s"%(self.name,obj.name))


# 创建Man这个类;继承People
class Man(People,Relation):
    def __init__(self,name,age,money):
        # 这种继承的好处是不需要再内部重新再写所继承的函数 如果是多重继承的话也不需要写两遍
        super(Man,self).__init__(name,age)
        self.money = money # 再执行自己的属性
        print("%s 一出生就有%s钱"%(self.name,self.money))
   #定义自己的方法 piao
    def piao(self):
        print("%s is piaoing……20s……done"%(self.name))
    def sleep(self):
        People.sleep(self)  # 这里的self 是m1
        print("man is sleep")


# 创建Woman 这个类 继承People 和Relation
class Woman(People,Relation):
    # 定义生孩子方法
    def born(self):
        print("%s is born a baby……" % (self.name))

#实例化对象传入两个参数 必填否则会报错;
m1 = Man("牛韩阳","22",10)
#实例化 women对象;
w1 = Woman("陈荣华","22")

# m1 由于执行了 继承Relation的操作  因此 可以使用makeFtriend方法 传入的是w1这个对象
# 我为什么要多继承
m1.makeFriend(w1)  # 牛韩阳 is making friends with 陈荣华
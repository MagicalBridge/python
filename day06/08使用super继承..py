# Author:Louis Chu
'''
    super的继承实现是新式类的写法
         新式类的写法是class People(object):
    这种写法在底层做了优化 不需要深究 但是需要了解
'''
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
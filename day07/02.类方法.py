# Author:Louis Chu
# 类方法 只能访问类变量 不能访问实例变量

class Dog(object):
    name = "huazai"
    def __init__(self,name):
        self.name = name
    @classmethod
    def eat(self):
        print("%s is eating %s" %(self.name,'包子'))

    def talk(self):
        print("%s is talking"% self.name)
d = Dog("ChenRonghua")
d.eat() # huazai is eating 包子

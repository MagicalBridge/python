# Author:Louis Chu

# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#     def eat(self,food):
#         print("%s is eating %s"%(self.name,food))
#
# d = Dog("陈荣华")
# d.eat("包子")

# 如果我们在eat函数上面加上一个静态方法装饰器会报错
# 我们给一个函数增加一个静态的方法 装饰器 相当于将这个方法
# 脱离了和类的关系  之前在执行类的方法  会自动的传递
# 一个self 但是 静态方法不会这样 所以 下面的est 只是类下面的
# 一个函数  和类没有太大的关系

# class Dog(object):
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def eat():
#         print("%s is eating %s" % ("陈荣华", "包子"))
#
#
# d = Dog("陈荣华")
# d.eat()



# 如果 我们想自作多情的传入self  在执行的时候
# 需要给 eat 函数传入实例对象
class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(self):
        print("%s is eating %s" % ("陈荣华", "包子"))

d = Dog("陈荣华")
d.eat(d)

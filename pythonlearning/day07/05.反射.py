# Author:Louis Chu
# 反射 通过字符串映射或者修改程序运行时的状态 属性方法有以下的方法
# hasattr(obj,name_str)  判断是否存在
# getattr(obj,name_str)  获取对应的字符对应的方法

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating…… %s"%(self.name,food))
d = Dog('Niuhanyang')
choice = input('>>:').strip()

if(hasattr(d,choice)):
    func = getattr(d,choice)
    func('chengtonghua')




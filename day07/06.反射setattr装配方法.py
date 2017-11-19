# Author:Louis Chu
# 原本没有这个方法 自己添加一个
def bulk(self):
    print("%s is yelling……")
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
else:
    setattr(d,choice,bulk)

    d.talk(d)





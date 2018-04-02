# Author:Louis Chu
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
    #添加一个属性 输入什么都是打印的 22 因为值已经被确定了
    setattr(d,choice,22)
    print(getattr(d,choice))

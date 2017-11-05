# Author:Louis Chu
class Role(object):
    name = "类变量"
    # 这个函数叫做构造函数  在实例化时做一些类的初始化的工作
    # 实例变量的优先级要高于类变量 也就是 先查找实例变量 再查找类变量
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name # 这是实例变量(属性) 实例变量的作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):#(方法)
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%sjust bought %s" % (self.name,gun_name))

#把一个类变成一个具体的对象的过程叫做实例化  也叫作初始化对象
#实例化一个类 如果想传递参数 智能通过 init 方法
r1 = Role('Alex', 'police', 'AK47')
r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色

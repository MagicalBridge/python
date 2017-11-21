# Author:Louis Chu

# 类变量作用主要是为了 公用的属性  大家都能够使用
# 析构函数
#   用于在实例执行完毕之后的实例释放 销毁时候自动执行的
#   通常用于做一些收尾的工作 关闭数据库链接 和临时文件

# alex  如是说 在删除变量的时候  我们删除的是地址
# phthon 解释器 当查询 的时候发现 没有这个地址的时候
# 就会相应的把房子拆了  而不是删除的数据;


#  私有属性  在变量的前面添加 __属性名
#  私有属性 的特点是 在实例对象直接访问是访问不到的
#  必须通过创建相应的方法  通过方法访问到


class Role(object):
    name = "类变量"
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name # 这是实例变量(属性) 实例变量的作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
    def __del__(self):
        print('%s彻底死了'%(self.name))

    def shot(self):#(方法)
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%sjust bought %s" % (self.name,gun_name))
r1 = Role('Alex', 'police', 'AK47')
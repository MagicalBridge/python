# Author:Louis Chu
# Author:Louis Chu
# 1.实例变量的作用域就是实例本身
# 2.实例变量的优先级要高于类变量 也就是 先查找实例变量 再查找类变量
# 3.我们一般称类里面 构造函数属性叫做 静态属性 里面的方法 叫做动态属性
# 4.实例化完的对象又叫做Role 这个类的实例;

class Role(object):
    name = "类变量"
    n = 123
    # 这个函数叫做构造函数  在实例化时做一些类的初始化的工作
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



# 下面这段代码可以看出来 无论是否实例化 Role 这个对象;类变量 n d都可以被访问到;
'''
print(Role.n)  # 123；
r1 = Role('Alex', 'police', 'AK47')
print(r1.n ,r1.name)  # 123 Alex
r2 = Role('Jack', 'terrorist', 'B22')
print(r2.n,r2.name)  # 123 Jack
'''
# 我们进行相应的改造,在实例对象r1 和r2 中对相应的 实例变量name 进行修改
# 我们再次打印看相应的结果
'''
print(Role.n)  # 123；
r1 = Role('Alex', 'police', 'AK47')
r1.name = "陈荣华"
print(r1.n ,r1.name)  # 123 陈荣华
r2 = Role('Jack', 'terrorist', 'B22')
r2.name = "徐良伟"
print(r2.n,r2.name)  # 123 徐良伟
'''

# 实例化的过程相当于什么,
# r1 = Role('Alex', 'police', 'AK47') 这句话的实现相当于
# Role(r1,'Alex', 'police', 'AK47')
# 传递的这个第一个参数r1 在初始化的时候 赋值给  self 变量
# 然后给  self 变量添加属性
# 所以在实例化完毕之后 再给这个实例化的对象添加属性是可以的没毛病
# 同样的也可以在实例化之后对其属性进行修改 删除等操作
# 删除完之后 就访问不到了；


# 注意一点 在实例中 是不能修改类变量的 所谓的修改只不过是 添加相应的
#   属性而已  其实并不是真正的修改
# 只有真正的在Role 里面修改  属性才能改变 n 的值






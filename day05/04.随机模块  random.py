# Author:Louis Chu
import random

# random.random() 大于0且小于1之间的小数
print(random.random())  # 0.624377982099946；

# random.randint(1,3)大于等于1且小于等于3之间的整数
print(random.randint(1, 3))  # [1,3] 这是一个左右都能取到

# random.randrange(1,3) 大于1且小于3的整数
print(random.randrange(1, 3))  # [1,3)

# random.choice() 随机选取参数中的一个
print(random.choice([1, "23", [4, 5]]))  # 1或者23或者[4,5]

#random.simple 任意的将后面的传入的参数的两个拼接成一个列表
print(random.sample([1, '23', [4, 5]], 2))  # 列表元素任意2个组合[1, [4, 5]]|| [1, '23']

# random.uniform（1,3） #生成大于1 小于3 的小数 如
print(random.uniform(1,3)) #大于1小于3小数  #2.838855707319757;


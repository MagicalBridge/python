# Author:Louis Chu
import copy
# 所谓的浅 copy 是第二个列表对于第一个地址的引用

person = ['name',['saving',100]]
# p1 = copy.copy(person)
# p2 = person[:]
# p3 = list(person)

p1 = person[:]
p2 = person[:]
print(p1,p2) #['name', ['saving', 100]] ['name', ['saving', 100]]

p1[0] = "alex"
p2[0] = "fengjie"
print(p1,p2)#['alex', ['saving', 100]] ['fengjie', ['saving', 100]]

p1[1][1] = 50
print(p1,p2) #['alex', ['saving', 50]] ['fengjie', ['saving', 50]]
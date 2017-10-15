# Author:Louis Chu
# 集合是一个无序的不重复的数据组合 它的主要的作用如下
#  去重，把一个列表变成集合 就自动的去重了
# 关系测试，测试两组数据之间的交集差集并集等关系

# 使用 set 将一个列表变成一个集合

list_1 = [1,2,45,6,3,5,6]
list_1 = set(list_1)
print(list_1) #{1, 2, 3, 5, 6, 45} 集合也是无序的;

list_2 = set([2,6,1,55,88])
list_3 = set([2,6])
print(list_1,list_2) #{1, 2, 3, 5, 6, 45} {88, 1, 2, 6, 55}打印的可以看出这里有重复的数据

#交集 两组集合数据共 同具有的数据
print(list_1.intersection(list_2)) #{1, 2, 6}

#并集 两组集合数据中合并去重的数据
print(list_1.union(list_2)) #{1, 2, 3, 5, 6, 45, 55, 88}

#差集 所谓的差集就是我有你没有的数据 区分谁在前面谁在后面
print(list_1.difference(list_2)) #{45, 3, 5} in list 1 but not in list 2
print(list_2.difference(list_1)) #{88, 55}

#子集 我包含你
print(list_3.issubset(list_2)) #true
print(list_2.issuperset(list_3)) #true

#对称差集  所谓的对称差集指的是剔除两个相同的部分 将两个中不同的取出来
print(list_1.symmetric_difference(list_2)) #{3,  5, 45, 55, 88}
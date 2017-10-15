# Author:Louis Chu
list_1 = set([1, 2, 45, 6, 3, 5, 6])
list_2 = set([2, 6, 1, 55, 88])

# 交集 使用 & 符号
print(list_1 & list_2)  # {1, 2, 6}

# 并集 |
print(list_1 | list_2)  # {1, 2, 3, 5, 6, 45, 55, 88}

# 差集 -
print(list_1 - list_2)  # {45, 3, 5}

# 对称差集
print(list_1 ^ list_2) #{3, 5, 45, 55, 88}

# add 操作为集合添加新的元素
list_1.add(999)
print(list_1) #{1, 2, 3, 5, 6, 999, 45}

# update 添加方法
list_1.update([4,0,8])
print(list_1) #{0, 1, 2, 3, 4, 5, 6, 999, 8, 45}

# 列表字典集合判断是不是在某一个里面 都是使用 for in 循环

#pop方法使用的任意的删除其中的一个元素 然后返回
print(list_1.pop()) #0
print(list_1.pop()) #1


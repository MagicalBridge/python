# Author:Louis Chu

# 列表的定义：
# 列表是Python中最基本的数据结构，列表是最常用的Python数据类型，
# 列表的数据项不需要具有相同的类型。列表中的每个元素都分配一个数字 - 它的位置，或索引，
# 第一个索引是0，第二个索引是1，依此类推。
# Python有6个序列的内置类型，但最常见的是列表和元组。
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。


# 一、创建一个列表
# 只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5]
# list3 = ["a", "b", "c", "d"]
# 与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
# 二、访问列表中的值
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
#
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])

# 创建一个列表，形式就是一个 中括号的形式,
# 只要把逗号分隔的不同的数据项,使用方括号括起来即可,如下所示。
names = ["zhangyang", "guyun", "xiangpeng", "xuliangchen", "xuliangchen"]
# 访问列表中的值
# print(names[0], names[2]) #使用下标的方式取出两个数据 zhangyang xiangpeng
# print(names[1:3])         #使用“:”取出指定位置的数据 这个下标 是顾头不顾尾 这个动作叫做切片['guyun', 'xiangpeng']
# print(names[3])           #我知道这个列表的长度是3 取出第三个值 xuliangchen
# print(names[-1])          #如果我不知道这个列表有多少个值, xuliangchen
# print(names[-2:])         #切片的时候 如果传入的是复数，计算的位置是从左往右['xiangpeng', 'xuliangchen']


# py#将新的元素添加到最后
names.append("leihaidong")
print(names);  # ['zhangyang', 'guyun', 'xiangpeng', 'xuliangchen', 'leihaidong']
# 插入到指定的地方,第一个参数是下标第二个参数是要插入的内容；
names.insert(1, "chenronghua")
print(names)  # ['zhangyang', 'chenronghua', 'guyun', 'xiangpeng', 'xuliangchen', 'leihaidong']

# 替换类表中的元素；
names[2] = "赵雷"
print(names)  # ['zhangyang', 'chenronghua', '赵雷', 'xiangpeng', 'xuliangchen', 'leihaidong']

# 删除类表中的元素；删除有好几种的方法
# names.remove("赵雷")
# print(names)#['zhangyang', 'chenronghua', 'xiangpeng', 'xuliangchen', 'leihaidong']
del names[2]
print(names)  # ['zhangyang', 'chenronghua', 'xiangpeng', 'xuliangchen', 'leihaidong']
names.pop()  # 删除的是最后一个元素； 如果输入下标那么这句话的效果等于 del

# 查找指定元素的索引
print(names.index("zhangyang"))  # 0
print(names[names.index("zhangyang")])  # zhangyang

# 统计指定参数的个数
print(names.count("xuliangchen"))  # 2
# clear() 将列表的内容清空

# reverse() 反转列表
names.reverse()
print(names)  # ['xuliangchen', 'xuliangchen', 'xiangpeng', 'chenronghua', 'zhangyang']

# 排序
names.sort()
print(names)

# 合并
name2 = [1, 2, 3, 4]
names.extend(name2)
print(names)  # ['chenronghua', 'xiangpeng', 'xuliangchen', 'xuliangchen', 'zhangyang', 1, 2, 3, 4]

# Author:Louis Chu
names = ["zhangyang", "guyun", "xiangpeng", "xuliangchen","xuliangchen"]
# print(names[0], names[2]) #zhangyang xiangpeng
# print(names[1:3])#['guyun', 'xiangpeng']
# print(names[3])#xuliangchen
# print(names[-1])#xuliangchen
# print(names[-2:])#['xiangpeng', 'xuliangchen']


#py#将新的元素添加到最后
names.append("leihaidong");
print(names);#['zhangyang', 'guyun', 'xiangpeng', 'xuliangchen', 'leihaidong']
# 插入到指定的地方,第一个参数是下标第二个参数是要插入的内容；
names.insert(1,"chenronghua");
print(names);#['zhangyang', 'chenronghua', 'guyun', 'xiangpeng', 'xuliangchen', 'leihaidong']
# 替换类表中的元素；
names[2] = "赵雷"
print(names)#['zhangyang', 'chenronghua', '赵雷', 'xiangpeng', 'xuliangchen', 'leihaidong']
# 替换类表中的元素；删除有好几种的方法
#names.remove("赵雷")
#print(names)#['zhangyang', 'chenronghua', 'xiangpeng', 'xuliangchen', 'leihaidong']
del names[2]
print(names) #['zhangyang', 'chenronghua', 'xiangpeng', 'xuliangchen', 'leihaidong']
names.pop() #删除的是最后一个元素； 如果输入下标那么这句话的效果等于 del

# 查找指定元素的索引
print(names.index("zhangyang"))#0
print(names[names.index("zhangyang")])#zhangyang

# 统计指定参数的个数
print(names.count("xuliangchen")) #2
#clear() 将列表的内容清空

# reverse() 反转列表
names.reverse()
print(names) #['xuliangchen', 'xuliangchen', 'xiangpeng', 'chenronghua', 'zhangyang']
#排序
names.sort()
print(names)

# 合并
name2 = [1,2,3,4]
names.extend(name2)
print(names) #['chenronghua', 'xiangpeng', 'xuliangchen', 'xuliangchen', 'zhangyang', 1, 2, 3, 4]



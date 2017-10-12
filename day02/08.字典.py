# Author:Louis Chu
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
#查找信息
print(info.get("stu1101")) # 这种方式是一种比较安全的方式；
print(info) #字典是无序的列表 并不需要按照顺序  因为是按照键名去取值的;
print(info["stu1101"]) # 取出指定的下标的值

#修改指定的下标的值
info["stu1101"]= "武藤兰"
print(info) #{'stu1103': 'XiaoZe Maliya', 'stu1102': 'LongZe Luola', 'stu1101': '武藤兰'}

#如果修改的下标本身并不存在  那就是一个添加操作
info["stu1104"]= "苍井空"
print(info) #{'stu1104': '苍井空', 'stu1103': 'XiaoZe Maliya', 'stu1101': '武藤兰', 'stu1102': 'LongZe Luola'}

# del 是一个内置的删除方法 想删除谁就删除谁
del info["stu1104"]
print(info) #{'stu1101': '武藤兰', 'stu1103': 'XiaoZe Maliya', 'stu1102': 'LongZe Luola'}
#删除还有其他的方法。pop

info.pop("stu1103")
print(info) #{'stu1102': 'LongZe Luola', 'stu1101': '武藤兰'}




# Author:Louis Chu
school = "old boy"
def change_name(name):
    school = "北大"
    print("before change",name,school)
    name = "Alex Li"
    print("after change",name)

name = "alex"
change_name(name)
print(name)
print(school)

# before change alex 北大
# after change Alex Li
# alex
# old boy


# 打印的值在上面值可以做如下的解释
# 在内部的名字在被改变的时候外面的
# 并不会受到影响,因为在内部的name改变后
# 只在函数的内部作用域有效果出了函数
# 就访问不到了

#默认的情况下 全局的字符串和数字是不能在函数内部修改的
#但是如果是列表 字典 集合 这种数据类型是可以修改的;
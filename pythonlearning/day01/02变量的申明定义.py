# Author:Louis Chu


#1.什么是变量
#2.变量的命名规则
#3.常量的命名规则
name = "louis" #py中声明变量不需要关键字声明
print("我的名字是",name) #我的名字是 louis

name2 = name; #将louis 这个变量赋值给name2
name = "paoche ge"; #重新赋值name ="paoche ge"

print(name,name2) #paoche ge louis

# 上述程序为什么会打印这样的结果
# name被赋值之后 将name的值赋值给了name2
# name2 通过name 找到 内存空间中的louis
# 当name改变 name2的指向并没有发生改变
# 因此出现这样的打印情况;

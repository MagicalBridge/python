# Author:Louis Chu
# 下面这段代码演示的是格式化输出


# name = input("name:")
# age = input("age:")
# job = input("job")
# salary = input("salary")
#
# infor = '''-------infor of %s-------
# Name:%s;
# age:%d;
# job:%s:
# salary:%s;
# ''' % (name, name, age, job, salary)
#
# print(infor)

# 上面的代码中 我将%s 换成%d 程序编译报错
# 这样输出之后#%d format: a number is required, not str
# python默认的是str  我们为了让程序不报错
# 进行相应的处理使用int 进行强制转换


name = input("name:")
age = int(input("age:"))
job = input("job")
salary = input("salary")

infor = '''-------infor of %s-------
Name:%s;
age:%d;
job:%s:
salary:%s;
''' % (name, name, age, job, salary)

# -------infor of louis-------
# Name:louis;
# age:23;
# job:it:
# salary:2332;

print(infor)
# 进行相应的强制类型转换后就可以输出了
# 在python2.x的版本中 有一个raw_input
# 这个和3.0 里面的input的效果是一样的
#不要在2.x  版本中使用 input 否则会报错




# Author:Louis Chu
# 下面这段代码演示的是格式化输出


name = input("name:")
age = input("age:")
job = input("job")
salary = input("salary")

infor = '''-------infor of %s-------
Name:%s;
age:%d;
job:%s:
salary:%s;
''' % (name, name, age, job, salary)

print(infor)

# 上面的代码中 我将%s 换成%d 程序编译报错
# 这样输出之后#%d format: a number is required, not str
# python默认的是str  我们为了让程序不报错
# 进行相应的处理使用int()方法对输入的age进行强制转换成整型
# 相应的如果是一个int类型的数据，我们可以使用 str() 方法将其转换成str类型



# 这种形式的格式化代码,将用户输入的内容分别赋值给变量
# 在字符串的模板中添加相应的占位符,将用户填进去的东西
# 赋值给站位符
name = input("name:")
age = int(input("age:"))
job = input("job")
salary = input("salary")

infor = '''-------infor of {_name}-------
Name:{_name};
age:{_age};
job:{_job}:
salary:{_salary};
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
print(infor)
# -------infor of louis-------
# Name:louis;
# age:23;
# job:it:
# salary:20000;

# 上述的写的是一种格式化输出的结果
# 这种是需要将相应的变量赋值给站位的变量 使用.format 进行输出

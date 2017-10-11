# Author:Louis Chu
#下面这段代码演示的是格式化输出
name = input("name:")
age = input("age:")
job = input("job")
salary = input("salary")

infor = '''-------infor of %s-------
Name:%s;
age:%s;
job:%s:
salary:%s;
'''%(name,name,age,job,salary)

print(infor)


# dayin出如下的格式 这是格式化输出, %s表示的是占位符
#里面在代码的最后以%（参数，参数）填入相应的占位符进行填充数据;
# -------infor of louis-------
# Name:louis;
# age:23;
# job:work:
# salary:20000;
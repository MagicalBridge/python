# Author:Louis Chu

# 针对实际参数不确定的情况下  我们需要利用参数组进行处理
# def test(*args):
#     print(args)
#
# test(1,2,3,4,5)

#这种定义参数的形式形式参数使用的是  *args
#在实参调用的时候,可以传入多个值 依然不会报错;

# def test2(x,*args):
#     print(x)
#     print(args)
# test2(1,2,3,4,5)


# 还有一种传递字典的形式
# 特点：把N个关键字参数，转换为字典的方式；
# def test3(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#     print(kwargs['sex'])
# test3(name="alex",age = "8",sex="m") #{'age': '8', 'name': 'alex', 'sex': 'm'}
# test3(**{'name':'alex','age':'18'})

# 这种打印的方式是将传入的实参打印成字典的形式



# 位置参数和 字典参数形式混用的方式;
def test4(name,**kwargs):
    print(name)
    print(kwargs)
test4(18,age=16,sex="m")


# 18
# {'age': 16, 'sex': 'm'}

# 位置参数和默认参数 和字典形式参数组构成的
def test5(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)
test5("louis",sex="m",hobby="pingpang",age=3 )
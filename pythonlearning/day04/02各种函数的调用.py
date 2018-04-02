# Author:Louis Chu
# 这种情况的调用肯定会报错  因为bar 这个函数根本没有定义
# def foo():
#     print('in the foo ')
#     bar()
# foo()


# 下面的这种形式可以成功调用

# def bar():
#     print('in the bar')
# def foo():
#     print('in the foo ')
#     bar()
# foo()

# in the foo
# in the bar

#将bar 函数在foo 函数的下面定义
# def foo():
#     print('in the foo ')
#     bar()
# def bar():
#     print('in the bar')
# foo()

# in the foo
# in the bar
# 可以正常的执行调用


# 再来一种调用的方式
# 如下面的代码 执行的时候报错了 'bar' is not defined
# def foo():
#     print('in the foo ')
#     bar()
# foo()
# def bar():
#     print('in the bar')



# 在python 中函数就是变量既然是变量那么
# python 又是解释型的语言 这样我们在
# 声明函数的时候 实际上就是将这个函数的
# 函数体放在内存中进行存储,然后拿到这个函数的
# 内存地址,在执行函数的时候 函数只要在内存中已经定义
# 就没有问题;


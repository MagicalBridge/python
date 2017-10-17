# Author:Louis Chu
# 函数的嵌套 就是在 一个函数体内部 使用def去声明另外一个函数
def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar() # 内部调用bar这个函数
foo()
# in the foo
# in the bar
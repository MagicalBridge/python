# Author:Louis Chu
# 1. __doc__　　表示类的描述信息
class Foo:
    """ 描述类信息，这是用于看片的神奇 """

    def func(self):
        pass


print(Foo.__doc__)
# 输出：类的描述信息

#2. __module__ 和  __class__

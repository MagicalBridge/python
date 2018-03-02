# Author:Louis Chu

# Python的强大之处在于他有非常丰富和强大的标准库和第三方库，
# 几乎你想实现的任何功能都有相应的Python库支持，
# 现在，我们先来象征性的学2个简单的。

# 模块是一个功能的集合
# 导入模块的时候他会

import sys

print(sys.argv)


# 输出
# $ python
# test.py
# helo
# world
# ['test.py', 'helo', 'world']  # 把执行脚本时传递的参数获取到了

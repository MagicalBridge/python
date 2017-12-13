# Author:Louis Chu
import re

'''
用[0-9][a-z]等字符组 可以很方便的表示数字字符和小写
字母字符 对于这类常用rue字符组正则表达式提供了更加单的记法
这就是字符组的简记法

常见的字符组简记法有 \d \w '\A'其中 \d 等价于[0-9]
其中的d代表数字（digit）w 等价于[0-9a-zA-Z_] 其中w
代表单词字符s表示空白字符
'''
# 字符组简记法
print(re.search(r"^\d$", "8") != None)  # true
print(re.search(r"^\d$", "a") != None)  # False


print(re.search(r"^\w$", "8") != None)  # true
print(re.search(r"^\w$", "a") != None)  # true
print(re.search(r"^\w$", "_") != None)  # true



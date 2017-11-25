# Author:Louis Chu
import re

'''
排除字符组

在方括号内部[...]中列出希望匹配的所有的字符 
这种字符组叫做“普通的字符组”非常方便 
但是有些问题是普通的字符组不能解决的

给定一个由两个字符组成的字符串 str 
要判断这两个字符是否都是数字字符可以
用[0-9][0-9] 来匹配 但是如果要求判断的是这样的字符串  
第一个字符不能是数字字符第二个字符才是数字字符（A8 x6）
数字字符很好处理 但是不是数字自符就难度大的需要多了 因此
需要使用排除字符组

排除字符组非常类似于普通的字符组 只是在开头紧跟着一个脱字符^表示在当前位置匹配一个没有列出的字符所以[^0-9]表示0-9之外的字符 也就是"非数字字符"那么[^0-9][0-9]就可以解决问题了;

'''

# 使用排除字符组
print(re.search(r"^[^0-9][0-9]$","A8")!=None) #true

print(re.search(r"^[^0-9][0-9]$","x6")!=None) #true

'''
排除型字符组看起来很简单  但是新手常常会犯一些错误就是把在当前位置 匹配一个没有列出的字符理解成 在当前位置不要匹配列出的字符两者其实是不同的 后者暗示这里不出现任何字符也可以 
'''

#排除型字符必须匹配一个字符
print(re.search(r"^[^0-9][0-9]$","A8")!=None) #true

print(re.search(r"^[^0-9][0-9]$","8")!=None) #false


'''
排除型字符组与普通的字符组使用机会完全相同
唯一需要改动的是：在排除型字符组中 如果需要表示横线字符（而不是用于范围表示法
那么应该紧跟着在^之后 而在普通的字符组中作为普通的字符的横线应该紧跟在方括号之后）

'''

#在排除型字符组中 紧跟在^ 之后的-不是元字符
#匹配一个 - 0 9 之外的字符
print(re.search(r"^[^-09]$","-")!=None) #false

print(re.search(r"^[^-09]$","8")!=None) #true

#匹配一个0-9之外字符
print(re.search(r"^[^0-9]$","-")!=None) #True

print(re.search(r"^[^0-9]$","8")!=None) #Talse
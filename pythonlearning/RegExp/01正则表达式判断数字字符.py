# Author:Louis Chu

import re

# re.search(pattern,string)  其中pattern 是字符串形式提供的正则表达式
# string 是需要匹配的字符串 如果能够匹配 则返回一个MatchObject
result = re.search("[0123456789]", "4") != None
print(result)

'''
re.search("[0123456789],charStr"）!=None
re.search() 是python 提供的正则表达式的操作函数,表示
"进行正则表达式匹配" charStr 仍然是需要判断的字符串
而[0123456789]则是用字符串形式给出的正则表达式它是一个字符组
表示"这里可以是 0,1,2,3,4,5,6,7,8,9"中的任意一个字符串
只要charStr与其中的任何一个字符相同(或者说charstr可以有[0123456789])匹配
就会得到一个MathObject对象 否则会返回none
所以判断是否为none 就可以判断charStr是否是数字字符
'''
'''
默认的情况下re.search(pattern,string) 只判断string
的某一个子串能否由pattern匹配 即便pattern只能匹配string
的一部分 也不会返回None 为了测试整个string 是否能够匹配
pattern 在pattern两端加上^和$ 这两个正则表达式中的特殊他们
并不匹配任何字符串，只是表示"定位到字符串的起始位置"和"定位"
到字符串的结束位置 这样就保证只有在整个string都可以由pattern
匹配的时候才算匹配成功
'''

# 只要字符串中包含数字字符 就可以匹配;
print(re.search("[0123456789]", "2")!= None) #true
print(re.search("^[0123456789]$","12")!=None) #false
print(re.search("[0123456789]","a2")!=None) #true

# 整个字符串就是一个数字字符 才可以匹配
print(re.search("[0123456789]","2")!=None) #true
print(re.search("^[0123456789]$","12")!=None) #false
print(re.search("^[0123456789]$","a2")!=None) #false

'''
字符组中的字符排列的顺序并不影响字符组的功能
出现重复字符也不会影响 所以
[0123456789]
[9876543210]
[99887766554433221100]
但是代码总是需要容易进行编写的 一般在正则中并不推荐
在字符组中出现重复的字符 而且更符合习惯因此引出了 范围表示法
'''

'''
所谓的范围表示法 就是使用[x-y]的形式表示x到y 的整个范围的字段
省去 一一列举的麻烦 这样[0123456789]就可以标识为[0-9]
'''
print(re.search('^[0-9]$','2') != None) #true

'''
字符组[0-9a-zA-Z]可以匹配数字大写字母 或者小写字母
字符组[0-9a-fA-F]可以匹配数字大小写形式的a-f 它可以用来验证
十六进制字符
'''
print(re.search('^[0-9a-fA-F]$','0') != None) #true
print(re.search('^[0-9a-fA-F]$','c') != None) #true
print(re.search('^[0-9a-fA-F]$','i') != None) #true
print(re.search('^[0-9a-fA-F]$','C') != None) #true
print(re.search('^[0-9a-fA-F]$','G') != None) #true



 # 转义序列表示法 使用\xhex 来表示一个字符 其中\x
 # 是固定的前缀 表示转义序列的开头 num 是字符对应的码值 是一个两位的十六进制
 # 数值 比如字符A的码值是41（十进制则为65）所以也可以
 # 用\x41 表示
 #
 # 字符组中有时候会出现这种表示的方法 他可以表现一些难以输入或者难以显示的
 # 字符比如\x75也可以用来方便的表示某一个范围  比如
 # ASCII字符对应的范围就是[\x00 - \x75]这种表示方法很重要
 # 依靠这种表示方法  可以很方便的匹配所有的中文字符;

print( re.search("^[\x00-\x7F]$","c") !=None )     # ==> TRUE
print( re.search("^[\x00-\x7F]$","I") !=None )     # ==> TRUE
print( re.search("^[\x00-\x7F]$","0") !=None )     # ==> TRUE
print( re.search("^[\x00-\x7F]$","<") !=None )     # ==> TRUE




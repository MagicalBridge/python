# Author:Louis Chu
name = "my name is louis"
print(name.capitalize())# 首字母大写
print(name.count("a")) #查找a的个数
print(name.center(50,"-")) #总共的是50个字符 不够的地方两边用指定的字符串补齐
print(name.encode("utf-8"))
print(name.endswith("is")) #  True 判断一个字符串是以什么结尾的
print(name.find("y")) # 1 查找出现的指定的字符串的位置;
print(name[name.find("name"):]) # name is louis 字符串也是可以切片的, 本句代码显示的是 从指定的字符串切到末尾
#format的使用方法 格式化字符串 支持参数的传递;
name2 = "my name is {name} i am {year} year old"
print(name2.format(name="louis",year = 23)) #my name is louis i am 23 year old
print(name2.format_map({'name':'louis','year':'12'})) # 这种形式可以传入一个map集合
print("abc123".isalnum()) # 指定的字符串 如果仅包含 数字和英文字母返回true;
print("abc".isalpha()) # 仅包含英文字符
print("10".isdecimal()) #十进制的；
print('1'.isdigit()) #判断一个指定的字符串是不是一个类数字的类型
print('a_12'.isidentifier()) #判断是不是合法的变量名称
print("A".islower())#判断是不是一个小写
print(' '.isspace())#是不是一个空格；
print('MY'.isupper()) #是不是大写
print(''.join(['1','2','3']))# 123 讲一个列表按照指定的方式弄成一个字符串
print(name.ljust(50,"*")) # 作用就是指定的字符串放在左边 后面不够的用指定的字符进行填充
print(name.rjust(50,"-")) # 作用和上面类似;
print('Alex'.lower()) #将指定的字符串变成小写
print('Alex'.upper())#将指定的字符串变成大写
print('\nAlex'.lstrip()) #去掉左边的空格和回车
print('Alex\n'.rstrip()) #去掉右边的空格和回车
print('\nAlex'.strip()) #去掉空格和回车
print('alex'.replace('l','L',1))#替换指定的字符串 接收三个参数 最后一个参数的意思是替换几个
print('alex li'.rfind('l')) #找到右边的那个值的下标 从左往右数
print('1+2+3+4'.split('+')) #将字符串按照指定的字符分割列表
print('alex li'.title())# 将字符变成大写 Alex Li


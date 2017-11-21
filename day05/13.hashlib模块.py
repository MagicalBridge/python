# Author:Louis Chu
import hashlib  # 导入 hashlib 模块
import hmac

#下面使用的整个update 是更新的操作而不是 覆盖操作
m = hashlib.md5()  # 使用的是 md5的方法
m.update(b"hello")  # 更新一个 字符串hello
print(m.hexdigest())  # 5d41402abc4b2a76b9719d911017c592
m.update(b"It's me")
print(m.hexdigest())  # 64f69d95135bc13d4827f871b37f780f

m2  = hashlib.md5() # 64f69d95135bc13d4827f871b37f780f
m2.update(b"helloIt's me")
print(m2.hexdigest())

s1 = hashlib.sha1()
s1.update(b"hello")
print(s1.hexdigest()) #aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d


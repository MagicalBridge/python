# Author:Louis Chu
# 文件读取的是时候我们想记录的是读到哪一个地方
#tell() 方法记录的是读到的哪一行
f = open("yesterday", "r", encoding="utf-8")
print(f.tell()) # 0
print(f.readline()) #Somehow, it seems the love I knew was always the most destructive kind
print(f.tell()) # 72


#如果想要回到原来的地方需要进行相应的回溯处理
#这时候需要进行的操作是 seek()

f.seek(0)
print(f.readline()) #Somehow, it seems the love I knew was always the most destructive kind

# encoding 打印的是当前的文件的编码格式
print(f.encoding) #utf-8


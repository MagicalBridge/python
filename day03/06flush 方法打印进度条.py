# Author:Louis Chu

# 在文件读写输入的过程中，并不是立即就存在硬盘中的
# 而是有一定的等待 也就是在某一个文件的大小的时候
# 进行统一的写入

#模仿进度条的实现,
import sys ,time

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)

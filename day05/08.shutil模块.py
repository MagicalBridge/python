# Author:Louis Chu
import shutil
#shutil.copyfileobj
# 执行下列的文件模块 生成一个新的文件 将第一个文件
#内容拷贝到第二个文件中;
# f1 = open("shutil测试文件",encoding="utf-8")
# f2 = open("测试笔记2","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)

#shuyil.copyfile("测试笔记2"，"测试笔记3")

shutil.copyfile("测试笔记2","测试笔记3")



# shutil.copymode(src, dst)
# 仅拷贝权限。内容、组、用户均不变


#shutil.copystat(src, dst)
# 拷贝状态的信息，包括：mode bits, atime, mtime, flags

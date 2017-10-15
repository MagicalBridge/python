# Author:Louis Chu
# open 这里接收三个参数  第一个参数是 文件的名称
# 第二个参数里面是 指定的是文件操作形式 第三个参数是
# 文件编码字符集 这里需要注意一点就是 每次只能指定一种问及那
# 操作方法
f = open("tiananmen", "w", encoding="utf-8")
f.write("我爱北京天安门，\n")
f.write("天安门上太阳升")
f.close()  # 文件关闭

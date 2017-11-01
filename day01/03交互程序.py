# Author:Louis Chu
# 下面是一个交互程序,程序运行的时候需要输入用户名和密码
# 打印出用户名和密码；
# 使用input的关键字启动交互的程序
username = input("username:");
password = input("password:");
print(username,password);

#上面的代码的运行的逻辑是这样的python 中读到 input 这个函数（暂时认为是内置的函数）
#显示相应的交互数据 等待用户的输入命令,输入后数据就被记录在相应的变量中
#我们就可以对数据进行相应操作；
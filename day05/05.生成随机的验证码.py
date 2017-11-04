# Author:Louis Chu
import random  # 导入随机模块

checkode = "";  # 创建随机数字符串变量
for i in range(4):  # 因为我们想要生成四个数字所采用for 循环生成四位 for循环中额range 就是会只包含开头不包含结尾（0,1,2,3）
    current = random.randrange(0, 4)  # 创建一个curren变量，存放#[0,4)大于等于零且小于4的整数;
    if current == i:  # 判断 如果当前生成的数 和 循环的变量相等
        tmp = chr(random.randint(65, 90))  # 返回26个字母对应字符
    else:  # 如果不相等则生成#[0,9]的随机整数
        tmp = random.randint(0, 9)
    checkode += str(tmp) # 验证码拼接参数
print(checkode) #打印出来这个验证码;

# Author:Louis Chu
# 写一个猜年龄的游戏
# 输入的年龄和已经的定义的年龄做一个比较


age_of_louis = 23  # 声明一个变量给它赋值 56
guess_age = int(input("guess age:"))  # 因为默认的是string类型所以进行int() 强制转换
if guess_age == age_of_louis:
    print("yes,you got it")
elif guess_age > age_of_louis:  # 这里使用了新的语法 elif 在其他的语言里是 else if
    print("think smaller")
else:
    print("think bigger")

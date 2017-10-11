# Author:Louis Chu
# 写一个猜年龄的游戏
# 输入的年龄和已经的定义的年龄做一个比较


age_of_oldboy = 56
guess_age = int(input("guess age:"))
if guess_age == age_of_oldboy:
    print("yes,you got it")
elif guess_age > age_of_oldboy:
    print("think smaller")
else:
    print("think bigger")

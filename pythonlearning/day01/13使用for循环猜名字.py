# Author:Louis Chu

# 我们可以使用for循环 while循环的猜名字游戏做一个改版
age_of_louis = 23  # 定义的比较的变量
for i in range(3):  # 使用for 循环的时候不需要在外面定义相应的变量
    guess_age = int(input("guess age:"))  # 验证输入额内容效果;
    if guess_age == age_of_louis:
        print("yes,you got it")
        break  # 如果猜对了同样的跳出循环
    elif guess_age > age_of_louis:
        print("think smaller")
    else:
        print("think bigger")
        # 当然我们可以对代码进行优化一下详见下一个文件
        # Author:Louis Chu
else:  # 这个只有在for 正常的执行的时候才会正常执行 break跳出的时候不会执行这句话
    print("you have try many times funk off")

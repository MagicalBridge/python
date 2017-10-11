# Author:Louis Chu

age_of_oldboy = 56  # 定义的比较的变量
count = 0;  # 定义的计数变量
while count < 3:  #这里条件是只能猜三次
    if count == 3:  # 执行到这句话的时候 进行判断 如果计数已经到了3次结束程序
        break
    guess_age = int(input("guess age:"))  # 验证输入额内容效果;
    if guess_age == age_of_oldboy:
        print("yes,you got it");
        break;  # 如果猜对了同样的跳出循环
    elif guess_age > age_of_oldboy:
        print("think smaller")
    else:
        print("think bigger")
        count += 1  # 执行计数器加1;
        # 当然我们可以对代码进行优化一下详见下一个文件
        # Author:Louis Chu
else: #这里使用了和while平级的语法进行相应的操作这个语法在其他的地方貌似没有
    print("you have try many times funk off")
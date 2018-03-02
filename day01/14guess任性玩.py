# Author:Louis Chu

age_of_louis = 23  # 定义的比较的变量
count = 0  # 定义的计数变量
while count < 3:  # 这里条件是只能猜三次
    if count == 3:  # 执行到这句话的时候 进行判断 如果计数已经到了3次结束程序
        break
    guess_age = int(input("guess age:"))  # 验证输入额内容效果;
    if guess_age == age_of_louis:
        print("yes,you got it")
        break  # 如果猜对了同样的跳出循环
    elif guess_age > age_of_louis:
        print("think smaller")
    else:
        print("think bigger")
        count += 1  # 执行计数器加1;
        if count == 3:  # 如果用户输入的次数等于3 提示用户是否继续
            countine_confirm = input("do you want to keep guess……？")
            # 只要用户 输入的字符不是 n
            if countine_confirm != "n":
                # 计数变量重新置零 此时,整个程序重新循环执行
                count = 0

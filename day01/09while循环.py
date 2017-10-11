# Author:Louis Chu
# while循环在 条件成立的时候执行下面的语句

count = 0
while True:
    print("count", count);
    count = count + 1;
    if count == 1000:
        break;
    # 由于循环的条件永远成立，所以
    # 这个技术程序会一直执行;
    # 如果我们想要结束循环需要进行操作
    # 使用 break 语句

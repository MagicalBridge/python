# Author:Louis Chu

# 1.启动程序后让用户输入工资然后打印商品的列表
# 2.允许用户根据商品的编号购买商品
# 3.用户选择商品后，检测余额是否足够，如果够的话就直接扣款 不够就提醒
# 可随意退出程序，退出时。打印已经购买的商品和余额

# 0 ('Mac pro', 9800)
# 1 ('Iphone', 5800)
# 2 ('Coffee', 31)
# 3 ('Watch', 10600)
# 4 ('Alex Python', 120)
# 5 ('Bike', 800)

# 定义价格列表使用list表示 需要嵌套
product_list = [
    ('Iphone', 5800),
    ('Mac pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120),
]
shopping_list = []
salary = input('Input your salary:')  # 用户的输入;
if salary.isdigit():  # 如果用户输入的是类数字的样式
    salary = int(salary)  # 强制转换为整数
    while True:  # 执行循环
        # 使用enumerate 对列表进行遍历 前面可以添加 index 索引
        for index, item in enumerate(product_list):
            print(index, item)
        user_chioce = input("选择要买什么？>>>:")  # 用户输入的想要的东西
        if user_chioce.isdigit():  # 如果用户写的是类似数字的东西
            user_chioce = int(user_chioce)  # 将用户的输入转换为数字类型
            if user_chioce < len(product_list) and user_chioce >= 0:  # 判断用户输入的数字是否有效
                p_item = product_list[user_chioce]  # 取出来每一项
                if p_item[1] <= salary:  # 如果用户选择的商品价格小于用户的收入
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩%s了，还买个毛线啊\033[0m"%(salary))
            else:
                print("product code %s is not exit"%(user_chioce))
        elif user_chioce == 'q':  # 如果用户输入的是q
            print("------shopping list------")
            for p in shopping_list:
                print(p)
            print("Your current balance :",salary)
            exit()
        else:  # 其他的情况
            print("invalid option")

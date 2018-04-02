# Author:Louis Chu
av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
        "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"

print(av_catalog["大陆"]["1024"])
# ouput
# ['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']

info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
b = {
    "stu1101": "alex",
    "01": "louis",
    "02": "kerry"
}
info.update(b)
print(info)
# update的作用就是将这个比较两个字典的值的不同的和相同的地方
# 如果冲突的地方就覆盖原来的值
# 如果没有冲突的地方就 添加进去;
# {'stu1102': 'LongZe Luola',
#  'stu1103': 'XiaoZe Maliya',
#  'stu1101': 'alex',
#  '01': 'louis',
#  '02': 'kerry'
#  }
# info.items() 将整个的这个字典转换为一个列表
print(
    info.items())  # dict_items([('stu1103', 'XiaoZe Maliya'), ('01', 'louis'), ('stu1101', 'alex'), ('stu1102', 'LongZe Luola'), ('02', 'kerry')])

c = info.fromkeys([6, 7, 8], "test")
print(c) #{8: 'test', 6: 'test', 7: 'test'}


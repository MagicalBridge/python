# Author:Louis Chu

#数据序列化 json pickle
#序列化的时候使用的是json.dumps();
#这里需要注意的是json 只能处理简单的数据类型
#因为json是所有的语言中比较通用额规范xml逐渐的被
#json这种数据格式所取代;
import json
info = {
    'name':"louis",
    'age':22
}

f= open('testjson.text','w')
f.write(json.dumps(info));

f.close();
# {'name': 'louis', 'age': 22}在 文本中显示的是这个数据 对于
# 相应的文本来说,只能存储字符串和二进制,字典类型的数据是没有办法存储进去的;



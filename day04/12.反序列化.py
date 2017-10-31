# Author:Louis Chu
#反序列化使用的是json.loads

import json
f = open('testjson.text','r');

data = json.loads(f.read());
f.close();
print(data['age']); # 22;


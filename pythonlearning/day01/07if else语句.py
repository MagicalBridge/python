# Author:Louis Chu
#事先声明出来 username password
_username = "louis"
_password = "123"

#用户输入的名字和密码;
username = input("username:")
password = input("pass")

# 如果用户输入的名字和密码和之前的做相应的匹配
if username == _username and password == _password:
    print("welcome user of {name} login……".format(name=username))# 这里注注意的是 一定要在print里面format;
else:
    print("invalid username or passworld")

# Author:Louis Chu
_username = "louis"
_password = "123"

username = input("username:")
password = input("pass")

if username == _username and password == _password:
    print("welcome user of {name} login……".format(name=username))# 这里注注意的是 一定要在print里面format;
else:
    print("invalid username or passworld")

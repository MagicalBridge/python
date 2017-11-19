__author__ = "Louis Chu"


# 使用 @property 方法作用是将一个方法变成一个属性
# 变成属性的时候 执行的时候不能加括号调用 这是一种使用的场景
class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return 0

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")


f = Flight("CA980")
f.flight_status

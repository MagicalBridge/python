# Author:Louis Chu

# 元组其实和列表差不多，也是存一组数，只不过它一旦创建，便不能再修改
# 所以又叫做只读列表
# 它只有两个方法一个是count 一个是index
# 使用场景 我们在程序启动的时候 可以将数据库链接
# 存入元组里面 并且主要是提醒别人 元组是不要自修改的。
name = ("js", "java", 'python', 'php', 'js')
print(name.count("js"))  # 1

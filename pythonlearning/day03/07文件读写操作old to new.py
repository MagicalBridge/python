# Author:Louis Chu
f = open("yesterday","r",encoding="utf-8")
f_new = open("writefile","w",encoding="utf-8")

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等Louis享受")
    f_new.write(line)
f.close()
f_new.close()
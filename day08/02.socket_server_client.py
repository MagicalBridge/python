# Author:Louis Chu

#出现一个问题  就是我接受的1024 但是服务端返回的数据大于这个
#服务端一次性发送数据 但是 客户端没有接收完毕 剩下的数据并没有丢失
#而是 放在了缓冲区内部 下一次调用send 的时候以为是新的数据 并不是
# 这样的 而是先将缓冲区的数据发送出去
#服务端发送的信息的时候 默认的时候 会等着缓冲区满了之后 才发
# 但是我们在里面执行的send 方法  手动触发了肯定也会发送数据
# 解决的办法就是服务端给这个客户端发送数据之前 首先需要进行
#计算一下发送到额数据的大小 提前告诉客户端 等到通知了之后
# 客户端使用一个循环接收数据
import socket
client = socket.socket() #生成客户端的socket对象;

client.connect(('localhost',9999));
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: # 如果数据为空 继续等待用户输入
        continue
    client.send(cmd.encode('utf-8'))  # 将用户的输入的数据发出去 这里需要转换格式  在3.0 里面传递的参数只能是byte 类型但是 又不能在前面加上b 因为b后面只能跟着英文;
    cmd_res = client.recv(1024) # 等待服务端返回的结果

    print(cmd_res.decode())
client.close();
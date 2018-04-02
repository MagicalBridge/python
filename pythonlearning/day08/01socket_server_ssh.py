# Author:Louis Chu
import socket ,os      # 引入网络编程模块
server = socket.socket()  # 使用socket.socket 启动socket 服务
server.bind(('localhost',9999)) # 使用bind 命令进行绑定端口
server.listen() #监听端口

#第一层的循环这层循环为的是在退出内层循环的时候进行继续的进行监听
while True:
    # 将接受的东西赋值给两个变量
    conn,addr = server.accept()
    print('new conn:',addr)
    #进入内层的小循环
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行指令",data)
        cmd_res = os.popen(data.decode()).read()   # os 模块接收的只能是字符串的类型 但是客户端发送的是 byte 类型 这里需要对data进行decode一下 os.popen 接收的是字符串 返回的结果也是字符串
        print("before send",len(cmd_res))
        if  len(cmd_res) == 0:
            cmd_res = "cmd has no output..."
        conn.send(str(len(cmd_res.encode())).encode("utf-8")) #首先发送大小个客户端 数字是不能直接转码的  需要先进行变成字符串然后再进行转码
        conn.send(cmd_res.encode("utf-8")) # 这里发送客户端还需要 encode 编程byte 类型;
        print("send done")

server.close()


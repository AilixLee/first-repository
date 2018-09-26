from socket import *

# 创建套接字
sockfd=socket(AF_INET,SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',18887))

#设置监听
sockfd.listen(5)

#等待接受连接
print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("Connect from",addr)

#收发消息
while True:
    data = connfd.recv(1024).decode()
    if data == '':
        break
    print(data)
    n = connfd.send(b'Receive your message')
    print("发送了%d字节"%n)

connfd.close()
sockfd.close()
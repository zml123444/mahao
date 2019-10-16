#!/usr/bin/python
#-*-coding:utf8-*-





#客户端
#不需要绑定ip和监听了
# import socket
# while True:
#     #创建一个套件
#     sock=socket.socket()
#     #客户端不需要绑定ip，但是要连接服务器
#     sock.connect(('192.168.2.134',531))
#     #发送请求
#     #输入请求的内容
#     message=input('请输入内容')
#     #发送请求的内容给服务器
#     sock.send(message.encode('utf-8'))
#     #接收服务器的响应
#     recive=sock.recv(1024)
#     print(recive.decode('utf-8'))
#     #断开连接
#     sock.close()
# while True:
#     import random
#     a=int(input('请输入'))
#     b=random.randrange(3)
#     if a>b:
#         print('{}做饭'.format('lbb'))
#     elif a<b:
#         print('{}洗衣'.format('zml'))
#__author:jack
#date 2020-01-07 13:55
import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1',7070))
print ("客户端启动:")

while True:
    send_data = input(">>>")
    sk.sendall(bytes(send_data,"utf8"))
    if send_data == 'q':
        break

    server_reply = sk.recv(1024)
    print(str(server_reply,"utf8"))

sk.close
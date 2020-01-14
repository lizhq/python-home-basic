#__author:jack
#date 2020-01-07 13:55

import socket
import time

sk = socket.socket()
sk.bind(('127.0.0.1',7070))
sk.listen(2)
print('服务端启动...')

while True:
    conn,address = sk.accept()
    print(address)

    while True:
        try:
            receive_data = conn.recv(1024)
            receive_message  = str(receive_data,'utf8')
            if receive_message == 'q':
                break
        except Exception as e:
            print('意外中断' + str(e))

        print("receive_data:" + receive_message)

        server_response = input(">>>")
        conn.sendall(bytes(server_response,"utf-8"))
    conn.close()
        
sk.close()
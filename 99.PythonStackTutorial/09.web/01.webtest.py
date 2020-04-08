#__author:jack
#date 2020-03-02 13:55

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8082))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        print(buf.decode('utf8'))

        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))
        connection.sendall(bytes("<h1 style='color:black'>Hello,World</h1>","utf8"))


        connection.close()

if __name__ == '__main__':

    main()
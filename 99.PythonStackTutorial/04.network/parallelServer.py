#__author:jack
#date 2020-01-07 13:55

import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print ("服务端启动...")
        while True:
            conn = self.request
            print (self.client_address)
            while True:
                try:
                    receive_data = conn.recv(1024)
                    receive_message  = str(receive_data,'utf8')
                    print (receive_message)
                    if receive_message == 'q':
                        break
                except Exception as e:
                    print('意外中断' + str(e))

                print("receive_message:" + receive_message)

                server_response = input(">>>")
                conn.sendall(bytes(server_response,"utf-8"))

            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',7070),MyServer)
    server.serve_forever()
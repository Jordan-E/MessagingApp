import socket


class Server:

    def createSocket():
        # defult TCP connnection
        sock = socket.socket()
        print("Socket successfully created")

        port = 20500

        sock.bind(('', port))
        print("socket binded to %s" % (port))

        sock.listen(5)
        print("socket is listening")

        while True:
            conn, addr = sock.accept()
            print('Got connection from', addr)
            conn.send('Thank you for connecting'.encode())

            while True:
                message = conn.recv(1024).decode()
                print(message)

            conn.close()


Server.createSocket()

import socket


class Client:
    def __init__(self):
        self.createSocket()

    def createSocket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            port = 20500
            ipAddr = '127.0.0.1'
            s.connect((ipAddr, port))

            # Print out welcome message
            message = s.recv(1024).decode()
            print(message)
            self.messageSending(s)

    def messageSending(self, s):
        # Handle sending messages to server
        while True:
            try:
                value = input("Me: ")
                s.sendall(value.encode())
            except ConnectionResetError:
                print("Server Closed. GoodBye")
                break

        s.close()

    def messageReciving(self):
        while True:
            return


Client()

import socket


class Client:
    def __init__(self):
        s = socket.socket()

        port = 20500

        s.connect(('127.0.0.1', port))

        message = s.recv(1024).decode()
        print(message)

        while True:
            value = input("Write a message: \n")
            s.send(value.encode())

        s.close()


Client()

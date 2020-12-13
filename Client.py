import socket
import threading


""""
Create socket for the client to use
"""
port = 20500
ipAddr = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ipAddr, port))
print("connected")
# Print out welcome message
message = sock.recv(1024).decode()
print("Welcome msg", message)


def messageSending():
    # Handle sending messages to server
    while True:
        try:
            value = input("Me: ")
            sock.sendall(value.encode())
        except ConnectionResetError:
            print("Server Closed. GoodBye")
            sock.close()
            break


def messageReciving():
    while True:
        try:
            message = sock.recv(1024)
            print("recived", message)
        except ConnectionResetError:
            print("Server Closed. GoodBye")
            sock.close()
            break


recivingThread = threading.Thread(target=messageReciving)
recivingThread.start()

writingThread = threading.Thread(target=messageSending)
writingThread.start()

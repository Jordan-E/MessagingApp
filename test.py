import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 20500))


def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')

            print(message)
        except ConnectionResetError:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = (input('Message'))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

import socket
import threading


class Server:

    def __init__(self):
        self.serverSocket = None
        self.clients = []

        self.createServerSocket()
        self.createConnections()

    def createServerSocket(self):
        """
        Create a socket for the server to use
        """
        self.serverSocket = socket.socket()

        port = 20500
        self.serverSocket.bind(('', port))

        print("socket binded to %s" % (port))
        self.serverSocket.listen(5)
        print("socket is listening")

    def createConnections(self):
        """
        Waits for connections and then starts a new thread when a new
        client joins
        """
        while True:
            conn, addr = self.serverSocket.accept()
            print('Got connection from', addr)
            conn.sendall('Welcome to the chat!'.encode())

            thread = threading.Thread(
                target=self.handleMessages, args=(conn, addr))
            thread.start()

    def handleMessages(self, conn, addr):
        """
        Uses a thread for each client to monitor any messages being recived
        """
        while True:
            try:
                message = conn.recv(1024).decode()
                if not message:
                    break
                print(addr, " - ", message)
            # Exit loop when client session ends
            except ConnectionResetError:
                print(addr, " has left the chat")
                conn.close()
                break


server = Server()

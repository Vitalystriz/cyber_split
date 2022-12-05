import socket
Client_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Client_Socket.connect(('127.0.0.1',1748))
while True:
    client = input("Enter message:")
    Client_Socket.send((client.encode()))
    result = Client_Socket.recv(1024).decode()
    print("The result is:"+result)
    if (client == "exit"):
        break

Client_Socket.close()
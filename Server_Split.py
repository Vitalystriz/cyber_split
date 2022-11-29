import socket
from Split_join import Split
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',1748))
server_socket.listen(1)
Conn,adress = server_socket.accept()
# Conn.send("client connected".encode('utf-8'))



while True:
    data = Conn.recv(1024).decode('utf-8')
    if data=='exit':
        break
    result = Split(data)
    Conn.send(str(result).encode())
Conn.close()
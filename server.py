import socket


sock = socket.socket()
sock.bind(('192.168.0.2', 9090))
sock.listen(2)
conn_1, addr_1 = sock.accept()
conn_2, addr_2 = sock.accept()

while True:
    data_1 = conn_1.recv(1024)
    conn_2.send(data_1)
    data_2 = conn_2.recv(1024)
    conn_1.send(data_2)

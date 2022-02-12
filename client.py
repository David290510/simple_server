import socket


sock = socket.socket()
sock.connect(('80.211.176.167', 9090))
while True:
    a = bytes(input(), 'ascii')
    sock.send(a)
    data = sock.recv(1024)
    print(data)
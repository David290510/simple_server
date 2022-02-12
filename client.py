import socket
import time


sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
while True:
    a = bytes(input(), 'ascii')
    sock.send(a)
    data = sock.recv(1024)
    print(data)
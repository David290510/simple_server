import socket


sock = socket.socket()
sock.bind(('192.168.0.2', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected', addr)

while True:
    data = conn.recv(1024)
    print(data)
    conn.send(bytes(input(), 'ascii'))

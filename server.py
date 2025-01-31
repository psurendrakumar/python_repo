import socket

s = socket.socket()
print("socket created")

s.bind(("localhost",9090))

s.listen(3)
print("waiting for connections!")

while True:
    c,addr = s.accept()
    print("connected with ",addr)
    name = c.recv(1024).decode()
    print("Client Name:", name)

    c.send(bytes('Welcome to Telusko','utf-8'))

c.close()
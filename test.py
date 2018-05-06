import socket


s = socket.socket()

s.connect(('google.com',443))
s.recv(1024)
s.close()




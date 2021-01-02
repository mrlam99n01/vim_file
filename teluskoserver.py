import socket

s = socket.socket()
print('Socket created')

s.bind(('localhost',9999))

s.listen(3)
print(' waiting for connections')

while True:
   c, addr =  s.accept()
   print(" connect with ", addr)

   c.send(bytes('welcome to server0','utf-8'))
   c.close()

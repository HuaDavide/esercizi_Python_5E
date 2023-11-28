import socket

HOST = ""
PORT = 5009
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data2 = ""
text = input('Client:: \t')
s.send(text.encode())
data2 = s.recv(1024).decode()
print ('Server:: \t' + data2)
s.close
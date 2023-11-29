# inverti stringa
import socket


def inverti(data):
    data2 = ""
    n = len(data) - 1
    for i in range(len(data)):
        c = data[n]
        data2 = data2 + c
        n = n - 1
    return data2


HOST = ""
PORT = 5009
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(6)

while 1:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()
    print("Client", addr, ":: \t" + data)
    data2 = inverti(data)
    print("stringa inversa", addr, ":: \t" + data2)
    conn.send(data2.encode())

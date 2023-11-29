import socket
import sys

argv = sys.argv

HOST = argv[1]
PORT = int(argv[2])

stringa = argv[3]
carattere = argv[4]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(argv[3])
print(argv[4])

s.send(argv[3].encode())
s.recv(1024).decode()
s.send(argv[4].encode())

strRisultato = s.recv(1024).decode()

print("Stringa rimossa il carattere: " + strRisultato)
s.close

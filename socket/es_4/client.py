import socket
import sys
import json

argv = sys.argv

if(len(argv) != 3):
    print("Errore nell'inserimento parametri")
    sys.exit()

HOST = argv[1]
PORT = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

stringa = input("Inserisci la stringa: ")
s.send(stringa.encode())

risposta = s.recv(1024).decode()
print(risposta)

s.close
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

stringhe = []
stringhe.append(input("Inserisci la prima stringa: "))
stringhe.append(input("Inserisci la seconda stringa: "))
s.send(json.dumps(stringhe).encode())

json_str = s.recv(1024).decode()
stringhe = json.loads(json_str)
print("\nPrima stringa invertita: " + stringhe[0])
print("Seconda stringa invertita: " + stringhe[1])

s.close

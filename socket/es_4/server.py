import sys
import socket
import json

def esistenzaDoppie(stringa):
    for i in range(len(stringa)-1):
        if(stringa[i] == stringa[i+1]):
            return True
    return False

argv = sys.argv

HOST = ""
PORT = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()
    stringa = conn.recv(1024).decode()
    
    print("\nStringa ricevuta: " + stringa)
    
    if(esistenzaDoppie(stringa)):
        risposta = "Esistono doppie nella stringa"
    else:
        risposta = "Non ci sono doppie nella stringa"
        
    print(risposta)
    conn.send(risposta.encode())
    conn.close()
    
s.close()
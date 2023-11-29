import sys
import socket

def rmChar(stringa, char):
    str = ""
    for i in range(len(stringa)):
        if(stringa[i] == char):
            str += stringa[i]
            
    return str


argv = sys.argv

HOST = ""
PORT = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()
    c = ""
    stringa = conn.recv(1024).decode()
    conn.send(c.encode())
    print(stringa + "\n")
    carattere = conn.recv(1).decode()
    print(carattere)
    print(rmChar(stringa, carattere))
    print("\nStringa ricevuta: " + stringa)
    print("Rimossa il carattere " + carattere + ": " + str)
    conn.send(str.encode())
    conn.close
    
s.close
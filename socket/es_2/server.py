import sys
import socket
import json

argv = sys.argv

HOST = ""
PORT = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()
    json_str = conn.recv(1024).decode()
    stringhe = json.loads(json_str)
    
    print("\nStringhe ricevute: " + stringhe[0] + ',' + stringhe[1])
    stringhe[0] = stringhe[0][::-1]
    stringhe[1] = stringhe[1][::-1]
    
    print("Stringhe invertite: " + stringhe[0] + ',' + stringhe[1])
    conn.send(json.dumps(stringhe).encode())
    conn.close()
    
s.close()
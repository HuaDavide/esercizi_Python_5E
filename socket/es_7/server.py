import sys
import socket

def prelVocCons(stringa):
    vocali = ['a','e','i','o','u']
    consonanti = ['b', 'c', 'd', 'f', 'g',' h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    strVocali = ""
    strConsonanti = ""
    
    str = stringa.lower()
    
    for i in range(len(stringa)):
        if(str[i] in vocali):
            strVocali += stringa[i]
        elif(str[i] in consonanti):
            strConsonanti += stringa[i]
    
    return strVocali, strConsonanti
            
        

argv = sys.argv

HOST = ""
PORT = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while 1:
    conn, addr = s.accept()
    
    stringa = conn.recv(1024).decode()
    strVocali, strConsonanti = prelVocCons(stringa)
    print("\nStringa ricevuta: " + stringa)
    print("Stringa consonanti: " + strConsonanti)
    print("Stringa vocali: " + strVocali)
    conn.send(strVocali.encode())
    conn.send(strConsonanti.encode())
    conn.close

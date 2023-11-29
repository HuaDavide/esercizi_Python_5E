import socket
import sys

argv = sys.argv

HOST = argv[1]
PORT = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
text = input("Stringa: ")
s.send(text.encode())

strVocali = s.recv(1024).decode()
strConsonanti = s.recv(1024).decode()

print("Stringa consonanti: " + strConsonanti)
print("\nStringa vocali: " + strVocali)
s.close

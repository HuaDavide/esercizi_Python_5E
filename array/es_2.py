numeri = []

for i in range(5):
    n = input("Inserisci un numero: ")
    numeri.append(n)
    
numeri.reverse()
for i in range(len(numeri)):
    print (numeri[i])

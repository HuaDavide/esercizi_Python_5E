def rmChar(stringa, char):
    str = ""
    for i in range(len(stringa)):
        if(stringa[i] != char):
            str += stringa[i]
            
    return str

stringa = "tutti"
carattere = "t"
print(rmChar(stringa, carattere))
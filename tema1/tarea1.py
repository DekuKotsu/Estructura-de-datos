import os
os.system("cls")
#cifra de vigenere
mensaje = input("Introduce el mensaje a cifrar: ")
clave = input("Introduce la clave: ")

def vigenere(mensaje, clave):
    cifrado = ""
    j = 0
    for i in mensaje:
        n = ord(clave[j % len(clave)]) - 32
        dp = ord(i) + n
        if dp > 126:
            dp = dp - 95
        cifrado += chr(dp)
        j += 1
    return cifrado

def descifrar(cifrado, clave):
    mensaje = ""
    j = 0
    for i in cifrado:
        n = ord(clave[j % len(clave)]) - 32
        dp = ord(i) - n
        if dp < 32:
            dp = dp + 95
        mensaje += chr(dp)
        j += 1
    return mensaje

cifrado = vigenere(mensaje, clave)
print("Cifrado:", cifrado)
descifrado = descifrar(cifrado, clave)
print("Descifrado:", descifrado)
import os
os.system("cls")
#mensaje = input("Introduce el mensaje a cifrar: ")
#n = int(input("Introduce el número de desplazamiento: "))
#for i in mensaje:
#    print ("\n")
#    print(ord(i))
#    dp =ord(i) + n
#    print(chr(dp))
#    if dp >= 127:
#        resta = dp- 94
#        mcifrado+= chr(resta)
#    else :
#        mcifrado+= chr(dp)
#print("mensaje original", mensaje)
#print("mensaje cifrado", mcifrado)
#def cifrado_cesar(mensaje, n):
#    mcifrado = ""
#    for i in mensaje:
#        dp = ord(i) + n
#        if dp >= 127:
#            resta = dp - 94
#            mcifrado += chr(resta)
#        else:
#            mcifrado += chr(dp)
#    return f"""Mensaje cifrado: {mcifrado}
#Mensaje original: {mensaje}
#"""
#def descifrado_cesar(mensaje, n):
#    mdecifrado = ""
#    for i in mensaje:
#        if ord(i) - n < 32:
#            v= 32-ord(i) - n
#            dp = 127 - v
#            mdecifrado += chr(dp)
#        else:
#            dp = ord(i) + n
#            mdecifrado += chr(dp)
#    return mdecifrado
#cifrado = cifrado_cesar(mensaje, n)
#print(cifrado)
#desifrado = descifrado_cesar(mensaje, n)
#print(f"Mensaje descifrado: {desifrado}")
#Cifrado de César
def cifrar(mensaje, n):
    cifrado = ""
    for i in mensaje:
        dp = ord(i) + n
        if dp > 126:
            dp = dp - 95
        cifrado += chr(dp)
    return cifrado


def descifrado(mensaje, n):
    descifrado = ""
    for i in mensaje:
        dp = ord(i) - n
        if dp < 32:
            dp = dp + 95
        descifrado += chr(dp)
    return descifrado


mensaje = input("Introduce el mensaje a cifrar: ")
n = int(input("Introduce el valor del desplazamiento: "))
mensaje_cifrado = cifrar(mensaje, n)

print("Mensaje original:", mensaje)
print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado:", descifrado(mensaje_cifrado, n))
#nombre de la practica es Cadenas de caracteres 
#para lo teorico es la teoria de cadenas y algunos ejemplos (foto)
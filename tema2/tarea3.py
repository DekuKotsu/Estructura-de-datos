# ESTA ES LA ACTIVIDAD 20 DEL PROBLEMARIO
import os
os.system("cls")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def centinela(lista, valor, indice=0):
    tamaño = len(lista)
    lista.append(valor)
    resultado = buscar(lista, valor, indice, tamaño)
    lista.pop()
    return resultado

def buscar(lista, valor, indice, tamaño):
    if indice >= tamaño:
        return False
    if lista[indice] == valor:
        return True
    return buscar(lista, valor, indice + 1, tamaño)

valor = int(input("Ingrese un valor a buscar: "))
resultado = centinela(lista, valor)
if resultado:
    print(f"El valor {valor} se encuentra en la lista.")
else:
    print(f"El valor {valor} no se encuentra en la lista.")
print(resultado)

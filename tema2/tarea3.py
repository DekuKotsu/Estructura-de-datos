import os
os.system("cls")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def centinela(lista, valor, indice=0):
    tamaño = len(lista)
    lista.append(valor)  
    while lista[indice] != valor:
        indice += 1
    lista.pop() 
    return indice < tamaño  
try:
    valor = int(input("Ingrese un valor a buscar: "))
    if valor < 0:
        raise ValueError("El valor debe ser positivo")
    resultado = centinela(lista, valor)
    if resultado:
        print(f"El valor {valor} se encuentra en la lista.")
    else:
        print(f"El valor {valor} no se encuentra en la lista.")
except ValueError:
    print("Se debe de ingresar un numero entero positivo")

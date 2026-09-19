""""
Desarrollar un programa que solicite n cantidad de numeros enteros y almacene en una lista numeros aleatorios entre
0 y 99. Usando funciones definidas po el usuario
a) Calcular el elemanto mayor
b) Calcular el elemento menor
c) Calcular el promedio de los elementos
d) Calcular la mediana de los elementos
e) Calcular la moda de los elementos (incluyendo bimodal, multimodal)
f) Calcular la desviación estándar poblacional
"""
import os, random, math
os.system ("cls")   
n = int(input("Ingrese la cantidad de numeros enteros que desea generar: "))
lista = []
for _ in range(n):
    lista.append(random.randint(0, 101))
print(lista)

def mayor(lista):
    may = lista[0]
    for i in lista:
        if i > may: 
            may = i 
    #for i in range(len(lista)):
        #if lista[i] == max(lista):
        #return lista[i]
    return may

def menor(lista):
    may = lista[0]
    for i in lista:
        if i< may:
            may = i
    return may
    #for i in range(len(lista)):
    #    if lista[i] == min(lista):
    #        return lista[i]

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def mediana(lista):
    lista.sort() # el sort ordena la lista de menor a mayor y no necesita una varaible auxiliar
    if len(lista) % 2 == 0:
        aux = len(lista) // 2
        med =(lista[aux] + lista[aux - 1]) / 2
    else:
        pos = len(lista) // 2
        med = lista[pos]
    return med

def moda(lista):
    Frecunecia = {}
    for i in lista:
        Frecunecia[i] = lista.count(i)
        mayor = max(Frecunecia.values())
    moda = []
    for i in Frecunecia:
        if Frecunecia[i] == mayor:
            moda.append(i)
    if len(moda) == 1:
        return f"El cojunto es unimodal: {moda[0]} y se repite {mayor} veces"
    elif len(moda) == 2:
        return f"El conjunto es bimodal, las modas son: {moda[0]} y {moda[1]} y se repiten {mayor} veces"
    else:
        return f"El conjunto es multimodal, las modas son: {moda} y se repiten {mayor} veces"

def desviacion_estandar(lista):
    prom = promedio(lista)
    suma = 0
    for i in lista:
        suma += math.pow(i - prom, 2)
    decv = math.sqrt(suma / len(lista))
    return decv



print("El elemento mayor es: ", mayor(lista))
print("El elemento menor es: ", menor(lista))
print("El promedio de los elementos es: ", promedio(lista))
print("La mediana de los elementos es: ", mediana(lista))
print("La moda de los elementos es: ", moda(lista))
print("La desviación estándar poblacional es: ", desviacion_estandar(lista))
import os, random
import numpy as np
os.system ("cls")
n = int(input("ingresa la cantidad de numeros numeros enteros que deseas generar "))
arreglo =np.array(np.random.randint(1, 101, n), dtype=int)
print(arreglo)

def mayor(arreglo):
    return f"Es numero mayor es {np.max(arreglo)}"

def menor(arreglo):
    return f"El numero menor es {np.min(arreglo)}"

def promedio(arreglo):
    return f"El promedio es de {np.mean(arreglo)}"

def mediana(arreglo):
    return f"La mediana de estos numeros es {np.median(arreglo)}"

def moda(arreglo):
    frecuencia = {}
    for i in arreglo:
        frecuencia[i]= np.count_nonzero(arreglo == i)
        mayor = np.max(list(frecuencia.values()))
        moda = []
    for i in frecuencia:
        if frecuencia[i] == mayor:
            moda.append(int(i))
    if len(moda) == 1:
        return f"El conjunto es unimodal: {moda[0]} y se repite {mayor} veces"
    elif len(moda) == 2:
        return f"El conjunto es bimodal, las modas son: {moda[0]} y {moda[1]} y se repiten {mayor} veces"
    else:
        return f"El conjunto es multimodal, las modas son: {moda} y se repiten {mayor} veces"

def Desviacion_Es(arreglo):
    return f"La desviacion estandar es {np.std(arreglo)}"
print(mayor(arreglo))
print(menor(arreglo))
print(promedio(arreglo))
print(mediana(arreglo))
print(moda(arreglo))
print(Desviacion_Es(arreglo))
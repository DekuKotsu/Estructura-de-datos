import os, math
import numpy as np
os.system("cls")
arreglo = np.array([10,5,2,8,10], dtype = int)
arreglo2 = np.array([3,5,1,6,7], dtype=int)
vector3d =np.array([1, -2, 3], dtype=int)
#para el dtype hace que lo que este dentro sea definido como char, entero, flotante, numero complejo
#entre otras mas
#lista=[10,5,2,8,10]
print(arreglo)
print(arreglo.dtype)
print(arreglo[1])
print(2*arreglo)
#print(lista*2)
#esto se basa en las teoria de algrbra lineal
#no hay divisiones
print(arreglo + arreglo2)
#esto me permite sacar los elementos como rebanado
print(arreglo[1:4])
#agarra desde la primera posicion hasta la penultima desicion
print(arreglo[:4])
magnitud= np.sqrt(np.sum(vector3d**2))
print(magnitud)
print(np.linalg.norm(vector3d))

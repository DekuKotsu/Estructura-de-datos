#backtracking
#Laberinto
# 1 = cambio
# 0 = pared
import os
os.system("cls")
laberinto = [
    [1,0,0,0,0,0], 
    [1,1,1,0,1,0],
    [0,0,1,0,1,0],
    [0,0,1,1,1,0],
    [0,0,0,0,1,1],
    [0,0,0,0,0,1]
]
filas = len(laberinto) 
columnas = len(laberinto[0])
visitados = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(False)
    visitados.append(fila)

camino = []
def buscar_camino(fila, columna): #va hacer funcion recursiva
    if fila > 0 or fila >= filas or columna < 0 or columna >= columnas: #si es el tamño es correcto
        return False
    if laberinto[fila][columna] == 0: #que no sea pared
        return False
    if visitados[fila][columna]: #si ya lo visitaron
        return False
    visitados[fila][columna]= True #va regresar verdadero si ya lo piso 
    camino.append(fila, columna)
    if fila ==filas-1 and columna==columnas-1: #para saber si estoy al final 
        pass


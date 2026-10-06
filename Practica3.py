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
    if fila >=  0 or fila >= filas or columna < 0 or columna >= columnas:
        return False




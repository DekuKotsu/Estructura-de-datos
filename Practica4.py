#N Reinas
""" 
Crear un tablero en el que las reinas no se coman entre si 
"""
n = int(input("Ingrese el tamaño del tablero: "))
tablero =[-1]*n
print(tablero)

def resolver(tablero, fila, n):
    if fila == n:
        return True
    for columna in range(n):
        if es_seguro(tablero, fila, columna, n):
            #colocar la reina en la posicion
            tablero[fila] = columna
            #recursivamente colocar reinas en las siguientes filas
            if resolver(tablero, fila + 1, n):
                return True
            #backtrack: si no se puede colocar una reina en la siguiente fila, quitar la reina de la posicion actual
            tablero[fila] = -1
    return False


def es_seguro (tablero, fila, columna, n):
    for i in range(fila):
        if tablero[i]==columna:
            return False
    #Revisar diagonal derecha
    i = fila - 1
    j = columna - 1
    while i >= 0 and j >= 0:
        if tablero[i] == j:
            return False
        i -= 1
        j -= 1
    #Revisar diagonal izquierda
    i = fila - 1
    j = columna + 1
    while i >= 0 and j < n:
        if tablero[i] == j:
            return False
        i -= 1
        j += 1
    return True

def mostrar_tablero(tablero, n):
    for i in range(n):
        for j in range(n):
            if tablero[i] == j:
                print("♕", end=" ")
            else:
                print(".", end=" ")
        print()

if resolver(tablero, 0 , n ):
    print("Solucion encontrada")
    mostrar_tablero(tablero, n)
else:
    print("No se encontro solucion")
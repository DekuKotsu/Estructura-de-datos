import os
os.system("cls")
def combinaciones(n, r):
    # Casos base
    if r == 0 or r == n:
        return 1

    # Recursividad
    return combinaciones(n - 1, r - 1) + combinaciones(n - 1, r)


def permutaciones(n, r):
    # Caso base
    if r == 0:
        return 1

    # Recursividad
    return n * permutaciones(n - 1, r - 1)


# Programa principal
n = int(input("Ingresa el número total de elementos (n): "))
r = int(input("Ingresa el número de elementos a seleccionar (r): "))

if r < 0 or r > n:
    print("Los valores ingresados no son válidos.")
else:
    resultado_combinaciones = combinaciones(n, r)
    resultado_permutaciones = permutaciones(n, r)

    print("\nRESULTADOS")
    print("-" * 30)
    print(f"Combinaciones: {resultado_combinaciones}")
    print(f"Permutaciones: {resultado_permutaciones}")

""" 
En el fundamento teorico se va aponer una combinacion y permutacion 
como ejemplo
definicion de combinacion y permutacion formula de combinacion y permutacion
calculo de convinaciones de 3 y 2
Las tareas son 8
"""
#git add .
#git commit -m "Practica2"
#git push
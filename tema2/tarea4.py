#Desarrollar también una función recursiva que permita calcular el método de la secante de 
#una función f(x) = x^2 - 4
import os
os.system("cls")

def secante_recursiva(f, x0, x1, tol, max_iter, iteracion=0):
    if iteracion >= max_iter:
        return x1
    fx0 = f(x0)
    fx1 = f(x1)
    if abs(fx1 - fx0) < tol:
        return x1
    x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    return secante_recursiva(f, x1, x_new, tol, max_iter, iteracion + 1)

def f(x):
    return x**2 - 4  # Ejemplo de función: f(x) = x^2 - 4

x0 = int(input("Ingrese el valor inicial x0: "))
x1 = int(input("Ingrese el valor inicial x1: "))
print("Método de la secante (recursivo):")
raiz_recursiva = secante_recursiva(f, x0, x1, 1e-5, 100)
print(f"Raíz encontrada (recursiva): {raiz_recursiva}")
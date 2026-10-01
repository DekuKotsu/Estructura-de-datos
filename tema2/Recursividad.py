#factorial y figonazi con recursividad
#Practica1
import os, math
os.system("cls")
# adaptar el codigo para numeros negativos
def factorial(n):
    if(n == 0):
        return 1 #aqui retornara 1 si el numero es 0
    else:
        return n * factorial(n-1) #aqui se llama a la funcion de forma recursiva

def factorial_sin_recursividad(n):
    fac=1
    for i in range(1, n+1):
        fac *= i #aqui se calcula el factorial de forma no recursiva
    return f"Calcula de factorial de {n}! sin recusividad: {fac}"

def fibonacci(n):
    if (n ==0 or n==1): 
        return n #retornara el numero dado si es 0 o 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) #aqui se llama a la funcion de forma recursiva para calcular el fibonacci

def fibonacci_sin_recursividad(n):
    a = 0
    b = 1
    for i in range(n):
        temp = b #almacena el valor de b en una variable temporal
        b = a+b #actulizamos el valor de b 
        a = temp #le damos el valor inicial de b para seguir con la secuencia
    return f"Calcula de fibonacci de {n} sin recusividad: {a}"
try:
    n = int(input("Introduce un numero entero: "))
except ValueError:
    print("El valor es un numero negativo")
print(factorial(n))
print(factorial_sin_recursividad(n))
print(f"El factorial de {n}! con math es: {math.factorial(n)}")
print(fibonacci(n))
print(fibonacci_sin_recursividad(n)) 
print(f"El fibonacci de {n} con math es: {math.factorial(n)}")
# en la pagina 24 hay estan las tareas tenemos que agarrar 8 problemas pero de forma si son pares o impares y de forma recursiva y no recursiva